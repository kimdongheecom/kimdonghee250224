SELECT * FROM member; #데이터 전체 확인하는 코드


SELECT email, name FROM member; #데이터 확인하는 코드(필요한 부분만)


SELECT email, name FROM member;

SELECT *
FROM member
WHERE email = 'ehdgml2754@gmail.com';
;


SELECT *
FROM member
WHERE email = 'test@test.com' AND password = '1234';

