Joey Yu IDS Assignment 5

![CI](https://github.com/yuyue1999/JoeyYu_IDS_Assignment5/actions/workflows/ci.yml/badge.svg)


Users after adding:
(1, 'Tom', 18)
(2, 'Jerry', 20)

Users after modifying age:
(1, 'Tom', 18)
(2, 'Jerry', 21)

Users after removing:
(1, 'Tom', 18)



(base) yy@Talking-Cats-MacBook-Pro JoeyYu_assignment5 % python -m pytest -cov=main test_main.py
========================================================================================================= test session starts ==========================================================================================================
platform darwin -- Python 3.12.4, pytest-7.4.4, pluggy-1.0.0
rootdir: /Users/yy/Downloads/ids706/JoeyYu_assignment5
configfile: ov=main
plugins: anyio-4.2.0
collected 3 items                                                                                                                                                                                                                      

test_main.py ...                                                                                                                                                                                                                 [100%]

========================================================================================================== 3 passed in 0.01s ===========================================================================================================