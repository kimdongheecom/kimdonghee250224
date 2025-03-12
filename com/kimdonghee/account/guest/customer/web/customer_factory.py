from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession

from com.kimdonghee.account.guest.customer.strategy.create_strategy import DefaultCreateCustomerStrategy, ValidateCreateCustomerStrategy
from com.kimdonghee.account.guest.customer.strategy.delete_strategy import HardDeleteCustomerStrategy, SoftDeleteCustomerStrategy
from com.kimdonghee.account.guest.customer.strategy.retrieve_strategy import GetAllStrategy, GetDetailStrategy
from com.kimdonghee.account.guest.customer.strategy.strategy_type import StrategyType
from com.kimdonghee.account.guest.customer.strategy.update_strategy import FullUpdateStrategy, PartialUpdateStrategy


class CustomerFactory:

    strategy_map = {
        StrategyType.DEFAULT_CREATE: DefaultCreateCustomerStrategy(),
        StrategyType.VALIDATE_CREATE: ValidateCreateCustomerStrategy(),
        StrategyType.GET_ALL: GetAllStrategy(),
        StrategyType.GET_DETAIL: GetDetailStrategy(),
        StrategyType.FULL_UPDATE: FullUpdateStrategy(),
        StrategyType.PARTIAL_UPDATE: PartialUpdateStrategy(),
        StrategyType.SOFT_DELETE: SoftDeleteCustomerStrategy(),
        StrategyType.HARD_DELETE: HardDeleteCustomerStrategy()
}

    @staticmethod
    async def execute(
        strategy: StrategyType, 
        method: Literal["create", "retrieve", "update", "delete"], 
        db: AsyncSession,
        **kwargs
    ):
        instance = CustomerFactory.strategy_map.get(strategy)
        if not instance:
            raise ValueError(f"Invalid strategy: {strategy}")
        
        if not hasattr(instance, method):
            raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")

        method_to_call = getattr(instance, method)

        # 비동기 메서드 여부 확인 후 실행
        if callable(method_to_call):
            if method == "retrieve":  # retrieve는 비동기 실행
                return await method_to_call(db=db, **kwargs)
            else:
                return await method_to_call(db=db, **kwargs)
        else:
            raise TypeError(f"Method '{method}' is not callable.")
