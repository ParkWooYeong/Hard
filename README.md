# Sparta Market - DRF
## accounts
**회원가입**

- endpoint : /api/accounts
- method : POST
![캡처](https://github.com/ParkWooYeong/Hard/assets/159976056/8bc39448-7279-4951-b42d-111a76e84bfc)

**토큰 재발급**
![Refresh토큰](https://github.com/ParkWooYeong/Hard/assets/159976056/69ebcb6b-f0d1-4bca-a1bc-67a126561189)


**로그인**
- endpoint : /api/accounts/login 
- method : POST
![로그인](https://github.com/ParkWooYeong/Hard/assets/159976056/5961eec3-b114-4014-be8e-fd5d65adfe36)

**로그아웃**
- endpoint : /api/accounts/logout 
- method : POST
![로그아웃](https://github.com/ParkWooYeong/Hard/assets/159976056/6cdca5de-da01-4979-aa63-9b9422a98404)

**프로필**
- endpoint : /api/accounts/<<str:username>> 
- method : GET
![프로필](https://github.com/ParkWooYeong/Hard/assets/159976056/09e56700-5212-41f5-93b2-9c9e826b33bd)

**프로필 수정**
- Endpoint : /api/accounts/<<str:username>> 
- Method : PUT
![프로필 수정](https://github.com/ParkWooYeong/Hard/assets/159976056/af8cafd0-ab7b-4497-9c2c-027d2e800404)


## products
**상품 등록**
- endpoint : /api/products
- method : POST
![생성](https://github.com/ParkWooYeong/Hard/assets/159976056/ac1fc2e3-e6aa-4b77-b04e-547541e39f58)

**상품 목록 조회**
- endpoint : /api/products
- method : GET
![조회](https://github.com/ParkWooYeong/Hard/assets/159976056/7fc71634-1dd8-4bd8-9049-271fd830a65d)

**상품 수정**
- endpoint : /api/products/<<int:productId>>
- method : PUT
![수정](https://github.com/ParkWooYeong/Hard/assets/159976056/bed178b3-a24f-4cde-8103-1424f9a05ae3)

**상품 삭제**
- endpoint : /api/products/<<int:productId>>
- method : DELETE
![삭제](https://github.com/ParkWooYeong/Hard/assets/159976056/6417819c-1689-4005-8c0c-85a01e9ccec4)

# ERD
![아니 이런가지고 drawio](https://github.com/ParkWooYeong/Hard/assets/159976056/ecb9712f-1648-4ba7-a168-3ba73a92b439)



