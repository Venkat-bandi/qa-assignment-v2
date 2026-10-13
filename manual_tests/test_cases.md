\# Manual Test Cases — ShopQA E-Commerce



\*\*Application Under Test:\*\* ShopQA (http://localhost:8000)

\*\*Tester:\*\* Venkat Bandi

\*\*Date:\*\* 2026-10-13

\*\*Test Type:\*\* Functional, Regression, Boundary



\---



\## 1. Test Scenarios Overview



| # | Scenario | Type | Priority |

|---|----------|------|----------|

| 1 | Register new user and login | Positive | High |

| 2 | Login with wrong password | Negative | High |

| 3 | Add single product to cart | Positive | High |

| 4 | Add multiple different products | Positive | Medium |

| 5 | Update quantity of existing product | Positive | Medium |

| 6 | Apply valid coupon (SAVE10) | Positive | High |

| 7 | Apply expired coupon (EXPIRED2020) | Negative | High |

| 8 | Apply invalid coupon (FAKE123) | Negative | High |

| 9 | Place order successfully | Positive | High |

| 10 | Add product with quantity = 0 | Boundary | High |

| 11 | Add product with quantity = -1 | Boundary | High |

| 12 | Add product with quantity = 9999 | Boundary | High |

| 13 | Add product with quantity = 10 (max) | Boundary | Medium |



\---



\## 2. Detailed Test Cases



\### TC-01 — Register a new user and login successfully



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-01 |

| \*\*Description\*\* | Verify a new user can register and then log in |

| \*\*Pre-conditions\*\* | None |

| \*\*Test Data\*\* | Unique email, Password: Test@123 |

| \*\*Steps\*\* | 1. Open Register page<br>2. Enter unique email + password<br>3. Confirm password<br>4. Click Register<br>5. Observe redirect to Login<br>6. Log in with registered credentials |

| \*\*Expected Result\*\* | Redirect to login page; login succeeds; lands on Products |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-02 — Login fails with wrong password



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-02 |

| \*\*Description\*\* | Verify login fails for invalid credentials |

| \*\*Pre-conditions\*\* | User is registered |

| \*\*Test Data\*\* | Email: testuser@shop.com, Password: WrongPass123 |

| \*\*Steps\*\* | 1. Open Login page<br>2. Enter valid email + wrong password<br>3. Click Login |

| \*\*Expected Result\*\* | Error message displayed; user stays on login page |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-03 — Add a single product to cart



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-03 |

| \*\*Description\*\* | Verify user can add a product and cart count updates |

| \*\*Pre-conditions\*\* | User is logged in |

| \*\*Test Data\*\* | Product: iPhone, Quantity: 1 |

| \*\*Steps\*\* | 1. Search iPhone<br>2. Set quantity=1<br>3. Click Add to Cart<br>4. Open cart page |

| \*\*Expected Result\*\* | Cart contains 1 item; iPhone displayed |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-04 — Add multiple different products



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-04 |

| \*\*Description\*\* | Verify multiple products can be added |

| \*\*Pre-conditions\*\* | User is logged in |

| \*\*Test Data\*\* | iPhone x1, MacBook x1 |

| \*\*Steps\*\* | 1. Add iPhone<br>2. Search MacBook<br>3. Add MacBook<br>4. Open cart |

| \*\*Expected Result\*\* | Cart contains 2 items |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-05 — Update quantity of an existing product



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-05 |

| \*\*Description\*\* | Verify quantity can be set on a product |

| \*\*Pre-conditions\*\* | User is logged in |

| \*\*Test Data\*\* | iPad, Quantity: 2 |

| \*\*Steps\*\* | 1. Search iPad<br>2. Set quantity=2<br>3. Add to cart<br>4. Open cart |

| \*\*Expected Result\*\* | Cart has 1 row with quantity=2 |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-06 — Apply valid coupon



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-06 |

| \*\*Description\*\* | Verify valid coupon applies 10% discount |

| \*\*Pre-conditions\*\* | User logged in, product in cart |

| \*\*Test Data\*\* | Coupon: SAVE10 |

| \*\*Steps\*\* | 1. Add iPhone to cart<br>2. Open checkout<br>3. Enter SAVE10<br>4. Click Apply |

| \*\*Expected Result\*\* | Coupon accepted; discount applied |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-07 — Apply expired coupon



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-07 |

| \*\*Description\*\* | Verify expired coupon is rejected |

| \*\*Pre-conditions\*\* | User logged in, product in cart |

| \*\*Test Data\*\* | Coupon: EXPIRED2020 |

| \*\*Steps\*\* | 1. Add iPhone to cart<br>2. Open checkout<br>3. Enter EXPIRED2020<br>4. Click Apply |

| \*\*Expected Result\*\* | Coupon rejected; discount remains -$0.00 |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-08 — Apply invalid coupon



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-08 |

| \*\*Description\*\* | Verify unknown coupon is rejected |

| \*\*Pre-conditions\*\* | User logged in, product in cart |

| \*\*Test Data\*\* | Coupon: FAKE123 |

| \*\*Steps\*\* | 1. Add iPhone to cart<br>2. Open checkout<br>3. Enter FAKE123<br>4. Click Apply |

| \*\*Expected Result\*\* | Coupon rejected; discount remains -$0.00 |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-09 — Place order successfully



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-09 |

| \*\*Description\*\* | Verify order can be placed successfully |

| \*\*Pre-conditions\*\* | User logged in, product in cart |

| \*\*Steps\*\* | 1. Add iPhone to cart<br>2. Open checkout<br>3. Click Place Order |

| \*\*Expected Result\*\* | Redirect to Orders page; at least 1 order visible |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-10 — Invalid Quantity: 0



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-10 |

| \*\*Description\*\* | Verify app rejects quantity=0 |

| \*\*Pre-conditions\*\* | User logged in |

| \*\*Test Data\*\* | Quantity: 0 |

| \*\*Steps\*\* | 1. Search iPhone<br>2. Set quantity=0<br>3. Add to Cart<br>4. Open cart |

| \*\*Expected Result\*\* | Item rejected; cart remains empty |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-11 — Invalid Quantity: -1



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-11 |

| \*\*Description\*\* | Verify app rejects negative quantity |

| \*\*Pre-conditions\*\* | User logged in |

| \*\*Test Data\*\* | Quantity: -1 |

| \*\*Steps\*\* | 1. Search iPhone<br>2. Set quantity=-1<br>3. Add to Cart<br>4. Open cart |

| \*\*Expected Result\*\* | Item rejected; cart remains empty |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-12 — Invalid Quantity: 9999



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-12 |

| \*\*Description\*\* | Verify app rejects quantity above max (10) |

| \*\*Pre-conditions\*\* | User logged in |

| \*\*Test Data\*\* | Quantity: 9999 |

| \*\*Steps\*\* | 1. Search iPhone<br>2. Set quantity=9999<br>3. Add to Cart<br>4. Open cart |

| \*\*Expected Result\*\* | Item rejected; cart remains empty |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\### TC-13 — Accept maximum allowed quantity (10)



| Field | Value |

|-------|-------|

| \*\*TC ID\*\* | TC-13 |

| \*\*Description\*\* | Verify app accepts maximum allowed quantity |

| \*\*Pre-conditions\*\* | User logged in |

| \*\*Test Data\*\* | Quantity: 10 |

| \*\*Steps\*\* | 1. Search iPhone<br>2. Set quantity=10<br>3. Add to Cart<br>4. Open cart |

| \*\*Expected Result\*\* | Cart contains 1 item with quantity=10 |

| \*\*Actual Result\*\* | As expected |

| \*\*Status\*\* | ✅ PASS |



\---



\## 3. Execution Summary



| Metric | Count |

|--------|-------|

| Total Test Cases | 13 |

| Passed | 13 |

| Failed | 0 |

| Pass Rate | 100% |

| Defects Logged | 1 (Remove button) |

