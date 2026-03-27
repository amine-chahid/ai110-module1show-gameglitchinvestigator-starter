# 💭 Reflection: Game Glitch Investigator

## 1. What was broken when you started?
While testing the game, I noticed that when I entered the number 1, the game sometimes told me to “go lower,” which didn’t make sense because 1 is already the minimum value. This helped me realize there was an issue with how the hint logic handled boundary cases. I also found that the game allowed out-of-range inputs, which could lead to confusing or incorrect feedback. I identified these bugs by playing the game multiple times and paying attention to inconsistent hints and behavior.

##2 How did you use AI as a teammate?

-I used Copilot Chat to analyze the relationship between app.py and logic_utils.py and understand how the hint logic was implemented. It correctly suggested that the issue might be related to missing edge case handling and lack of input validation. I also used Inline Chat to get step-by-step explanations of specific parts of the code, which helped me understand the logic more clearly. One misleading suggestion was that the issue could be caused by the random number generation, but I verified through testing that this was not the case.

3. Debugging and testing your fixes
I used pytest to verify that my fixes worked correctly. At first, the pytest command was not recognized, so I installed it using python -m pip install pytest and then ran the tests using python -m pytest. All three tests passed successfully, confirming that the check_guess function returns the correct results for "Too High", "Too Low", and "Win".

I also manually tested the game by running it with Streamlit and entering edge case values like the minimum number and out-of-range inputs. After adding validation, the game no longer produces incorrect hints and behaves as expected.

## 4. What did you learn about Streamlit and state?
I learned that Streamlit reruns the entire script every time the user interacts with the app, like when clicking a button or entering input. At first, this was confusing because it seemed like the game kept resetting, but I realized that session state is what keeps important data like the secret number and attempts from being lost. Without session state, the game wouldn’t be able to track progress between interactions. Understanding this helped me see how Streamlit manages interactivity in a simple but powerful way.

## 5. Looking ahead: your developer habits

One habit I want to reuse is testing my code more intentionally using pytest instead of just relying on manual testing. Writing small, focused tests helped me confirm that my logic was working correctly and gave me more confidence in my fixes. I also found it useful to break problems into smaller parts and ask AI specific questions instead of one big vague prompt. This made debugging faster and easier to understand.