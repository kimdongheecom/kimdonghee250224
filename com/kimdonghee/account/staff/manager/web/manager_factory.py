


from typing import Literal
from sqlalchemy.ext.asyncio import AsyncSession
from com.kimdonghee.account.staff.manager.services.create_strategy import DefaultCreateManagerStrategy, ValidateCreateManagerStrategy
from com.kimdonghee.account.staff.manager.services.delete_strategy import HardDeleteManagerStrategy, SoftDeleteManagerStrategy
from com.kimdonghee.account.staff.manager.services.retrieve_strategy import GetAllStrategy, GetDetailStrategy
from com.kimdonghee.account.staff.manager.services.update_strategy import FullUpdateStrategy, PartialUpdateStrategy
from com.kimdonghee.account.staff.manager.services.create_strategy import DefaultCreateManagerStrategy
from com.kimdonghee.account.staff.manager.services.strategy_type import StrategyType


class ManagerFactory:
        strategy_map = {
            StrategyType.DEFAULT_CREATE: DefaultCreateManagerStrategy(),
            StrategyType.VALIDATE_CREATE: ValidateCreateManagerStrategy(),
            StrategyType.GET_ALL: GetAllStrategy(),
            StrategyType.GET_DETAIL: GetDetailStrategy(),
            StrategyType.FULL_UPDATE: FullUpdateStrategy(),
            StrategyType.PARTIAL_UPDATE: PartialUpdateStrategy(),
            StrategyType.SOFT_DELETE: SoftDeleteManagerStrategy(),
            StrategyType.HARD_DELETE: HardDeleteManagerStrategy()
        }
        #생성전략을 준다는 것이다. 컨트롤러에서 URI를 보고 CreateStrategy를 만든다(인스턴스생성).

        @staticmethod
        async def execute(
            strategy: StrategyType, 
            method: Literal["create", "retrieve", "update", "delete"], 
            db: AsyncSession,
            **kwargs
        ):
            instance = ManagerFactory.strategy_map.get(strategy)
            if not instance:
                raise ValueError(f"Invalid strategy: {strategy}")
            
            if not hasattr(instance, method): #속성이 없으면 속성이 없다고 처리해야 한다.
                raise AttributeError(f"Strategy '{strategy}' does not have a '{method}' method.")

            method_to_call = getattr(instance, method)

            # 비동기 메서드 여부 확인 후 실행
            if callable(method_to_call):
                if method == "retrieve":  # retrieve는 비동기 실행
                    return await method_to_call(db=db, **kwargs)  # 동적으로 해당 메서드를 실행
                else:
                    return await method_to_call(db=db, **kwargs)
            else:
                raise TypeError(f"Method '{method}' is not callable.")
            #StrategyType은 메뉴판이다. 이 함수는 짜장면을 주문하는 것과 같다.
       

