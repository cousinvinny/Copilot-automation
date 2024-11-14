# CMPE 187 Copilot Test Script
# Authors: Vinh Nguyen
# Date: 5/14/24

import time
import spacy.cli
#spacy.cli.download("en_core_web_lg")
nlp = spacy.load("en_core_web_lg")

from appium import webdriver
from typing import Any, Dict
from appium.options.common import AppiumOptions
from appium.webdriver.common.appiumby import AppiumBy

def get_score(similarity):
    if similarity > .9:
        return "PASS"
    else:
        return "FAIL"


cap: Dict[str, Any] = {
    'platformName': 'Android',
    'automationName': 'uiautomator2',
    'deviceName': 'Android',
    'appPackage': 'com.scaleup.chatai',
    'appActivity': 'com.scaleup.chatai.MainActivity',
}

url = 'http://localhost:4723'

driver = webdriver.Remote(url, options=AppiumOptions().load_capabilities(cap))

#el = driver.find_element(by=AppiumBy.XPATH, value='//*[@content-desc="Skip"]')

#Getting past first screens
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Continue"]')
el.click()
time.sleep(2)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivClose"]')
el.click()
time.sleep(2)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/editTextChat"]')
el.click()


#Test Case 1
print("\n===Test Case #1===")
print("What is the formal definition of linear independence?\n")
input_text = "What is the formal definition of linear independence?"
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
#el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/mtvText"]')
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = """If 𝑆 = {v1, v2, . . . , vr} is a set of two or more vectors in a vector space 𝑉,
then 𝑆 is said to be a linearly independent set if no vector in 𝑆 can be expressed as a linear combination of the others.
A set that is not linearly independent is said to be linearly dependent. If 𝑆 has only one vector, we will agree that it
is linearly independent if, and only if that vector is nonzero
"""
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 2
print("\n===Test Case #2===")
print("Who created linear independence?\n")
input_text = "Who created linear independence?"
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = "The concept cannot be attributed to a single person"
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 3
print("\n===Test Case #3===")
print("""Tell me a joke
Is this matrix linearly independent: [(1, 1), (20, 1)]?""")
input_text = """Tell me a joke
Is this matrix linearly independent: [(1, 1), (20, 1)]?"""
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = "Linearly Independent"
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 4
print("\n===Test Case #4===")
print("""Is this matrix: [] linear independent?
""")
input_text = """Is this matrix: [] linear independent?"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "Cannot be determined"

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 5
print("\n===Test Case #5===")
print("""Tell me a joke
When was linear independence made?
""")
input_text = """Tell me a joke
When was linear independence made?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "Unknown"

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 6
print("\n===Test Case #6===")
print("""What is the formal definition of linear independence?
""")
input_text = """What is the formal definition of linear independence?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "A set of vectors {v1,v2,…,vk} is linearly independent if the vector equation x1v1+x2v2+⋯+xkvk=0 has only the trivial solution x1=x2=⋯=xk=0 . The set {v1,v2,…,vk} is linearly dependent otherwise."

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 7
print("\n===Test Case #7===")
print("""Independent linear matrix is: [(5, 500), (250, 15)]?
""")
input_text = """Independent linear matrix is: [(5, 500), (250, 15)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 8
print("\n===Test Case #8===")
print("""Was what Wronskian?
""")
input_text = """Was what Wronskian?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(15)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """If f1 = 𝑓1(x), f2 = 𝑓2(x), . . . , fn = 𝑓n(x) are functions that are n − 1 times differen-
tiable on the interval (−∞, ∞), then the determinant
𝑊(x) =
𝑓1(x) 𝑓2(x) ⋅ ⋅ ⋅ 𝑓n(x)
𝑓′
1 (x) 𝑓′
2 (x) ⋅ ⋅ ⋅ 𝑓′
n (x)
𝑓(n−1)
1 (x) 𝑓(n−1)
2 (x) ⋅ ⋅ ⋅ 𝑓(n−1)
n (x)
is called the Wronskian of 𝑓1, 𝑓2, . . . , 𝑓n."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 9
print("\n===Test Case #9===")
print("""Homogeneous Trivial Solution Theorem is for Linear Independence?
""")
input_text = """Homogeneous Trivial Solution Theorem is for Linear Independence?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 10
print("\n===Test Case #10===")
print("""Independent linear matrix is: [(1, 2), (2, 4)]?
""")
input_text = """Independent linear matrix is: [(1, 2), (2, 4)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Dependent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 11
print("\n===Test Case #11===")
print("""Independent is matrix linear: [(10, 20, 40), (40, 10, 20), (50, 30, 10)]?
""")
input_text = """Independent is matrix linear: [(10, 20, 40), (40, 10, 20), (50, 30, 10)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 12
print("\n===Test Case #11===")
print("""Independence Created of Linear
""")
input_text = """Independence Created of Linear
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """The concept cannot be attributed to a single person"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 13
print("\n===Test Case #13===")
print("""Tell me a joke
Linear is :[(10, 20, 40), (40, 10, 20), (50, 30, 10)] matrix independent?

""")
input_text = """Tell me a joke
Linear is :[(10, 20, 40), (40, 10, 20), (50, 30, 10)] matrix independent?

"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 14
print("\n===Test Case #14===")
print("""Tell me a joke
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """Tell me a joke
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 15
print("\n===Test Case #15===")
print("""Tell me a joke
Theorem Solution Homogeneou Trivial were what
""")
input_text = """Tell me a joke
Theorem Solution Homogeneou Trivial were what
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 16
print("\n===Test Case #16===")
print("""What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 17
print("\n===Test Case #17===")
print("""Tell me a joke
Linear is :[(-1, -2, -1), (1, 2, 1), (2, 4, 2)] matrix independent?
""")
input_text = """Tell me a joke
Linear is :[(-1, -2, -1), (1, 2, 1), (2, 4, 2)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 18
print("\n===Test Case #18===")
print("""Tell me a joke
Linear is :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] matrix independent?
""")
input_text = """Tell me a joke
Linear is :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 19
print("\n===Test Case #19===")
print("""Tell me a joke
Independence Linear made when?
""")
input_text = """Tell me a joke
Independence Linear made when?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Unknown"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 20
print("\n===Test Case #20===")
print("""Linr si :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] mtxx indiepeendan?
""")
input_text = """Linr si :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] mtxx indiepeendan?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#


#Test Case 21
print("\n===Test Case #21===")
print("""Si tis lnrly indpt -1, -2, -1), (1, 2, 1)2, 4, 2)]?
""")
input_text = """Si tis lnrly indpt -1, -2, -1), (1, 2, 1)2, 4, 2)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 22
print("\n===Test Case #22===")
print("""Linr si :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] mtxx indiepeendan?
""")
input_text = """Linr si :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] mtxx indiepeendan?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 23
print("\n===Test Case #23===")
print("""Wat is Wonskan?
""")
input_text = """Wat is Wonskan?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """If f1 = 𝑓1(x), f2 = 𝑓2(x), . . . , fn = 𝑓n(x) are functions that are n − 1 times differen-
tiable on the interval (−∞, ∞), then the determinant
𝑊(x) =
𝑓1(x) 𝑓2(x) ⋅ ⋅ ⋅ 𝑓n(x)
𝑓′
1 (x) 𝑓′
2 (x) ⋅ ⋅ ⋅ 𝑓′
n (x)
𝑓(n−1)
1 (x) 𝑓(n−1)
2 (x) ⋅ ⋅ ⋅ 𝑓(n−1)
n (x)
is called the Wronskian of 𝑓1, 𝑓2, . . . , 𝑓n.
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 24
print("\n===Test Case #24===")
print("""sI tis matrick: [] leanare indeependit?
""")
input_text = """sI tis matrick: [] leanare indeependit?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cannot be determined
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 25
print("\n===Test Case #25===")
print("""sI tis matrick: [] leanare indeependit?
""")
input_text = """Matrick sI tis: [] indeependit leanare ?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cannot be determined
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 26
print("\n===Test Case #26===")
print("""Hoo is Crater of Indeependthis Leanher?
""")
input_text = """Hoo is Crater of Indeependthis Leanher?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """The concept cannot be attributed to a single person
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 27
print("\n===Test Case #27===")
print("""Homogeneus triveel soulootion therem ish wat?
""")
input_text = """Homogeneus triveel soulootion therem ish wat?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 28
print("\n===Test Case #28===")
print("""Mayrix solf tis: []
""")
input_text = """Mayrix solf tis: []
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cannot be determined"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 29
print("\n===Test Case #29===")
print("""Is leaner indiependence formal deafinition?
""")
input_text = """Is leaner indiependence formal deafinition?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """If 𝑆 = {v1, v2, . . . , vr} is a set of two or more vectors in a vector space 𝑉,
then 𝑆 is said to be a linearly independent set if no vector in 𝑆 can be expressed as a linear combination of the others.
A set that is not linearly independent is said to be linearly dependent. If 𝑆 has only one vector, we will agree that it
is linearly independent if, and only if that vector is nonzero
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 30
print("\n===Test Case #30===")
print("""Mayduh leaner indiependant whun?
""")
input_text = """Mayduh leaner indiependant whun?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Unknown
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 31
print("\n===Test Case #31===")
print("""explain invertibility theorem linear algebra
""")
input_text = """explain invertibility theorem linear algebra
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """a square matrix a is invertible if and only if lambda = 0 is not an eigenvalue of A
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 32
print("\n===Test Case #32===")
print("""who made eigenvectors
""")
input_text = """who made eigenvectors
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Leonhard Euler
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 33
print("\n===Test Case #33===")
print("""
In Example 1 we observed that 𝜆 = 3 is an eigenvalue of the matrix
𝐴 = [3 0
8 −1]
but we did not explain how we found it. Use the characteristic equation to find all eigenvalues
of this matrix.
""")
input_text = """
In Example 1 we observed that 𝜆 = 3 is an eigenvalue of the matrix
𝐴 = [3 0
8 −1]
but we did not explain how we found it. Use the characteristic equation to find all eigenvalues
of this matrix.
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """This shows that the eigenvalues of 𝐴 are 𝜆 = 3 and 𝜆 = −1. Thus, in addition to the eigen-
value 𝜆 = 3 noted in Example 1, we have discovered a second eigenvalue 𝜆 = −1.
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 34
print("\n===Test Case #34===")
print("""
Find the eigenvalues of
𝐴 = [
0 1 0
0 0 1
4 −17 8
""")
input_text = """
Find the eigenvalues of
𝐴 = [
0 1 0
0 0 1
4 −17 8
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Thus, the eigenvalues of 𝐴 are
𝜆 = 4, 𝜆 = 2 + √3, and 𝜆 = 2 − √3
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 35
print("\n===Test Case #35===")
print("""
Find the eigenvalues of this 0x0 matrix
""")
input_text = """
Find the eigenvalues of this 0x0 matrix
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """eigenvalue of 0 and all non-zero vectors as your eigenvectors
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 36
print("\n===Test Case #36===")
print("""
Explain eigenspaces
""")
input_text = """
Explain eigenspaces
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Now that we know how to find the eigenvalues of a matrix, we will consider the problem of
finding the corresponding eigenvectors. By definition, the eigenvectors of 𝐴 correspond-
ing to an eigenvalue 𝜆 are the nonzero vectors that satisfy
(𝜆𝐼 − 𝐴) x = 0
Thus, we can find the eigenvectors of 𝐴 corresponding to 𝜆 by finding the nonzero vec-
tors in the solution space of this linear system. This solution space, which is called the
eigenspace of 𝐴 corresponding to 𝜆, can also be viewed as:
1. the null space of the matrix 𝜆𝐼 − 𝐴
2. the kernel of the matrix operator 𝑇𝜆 𝐼−𝐴∶ 𝑅n → 𝑅n
3. the set of vectors for which 𝐴x = 𝜆x
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 37
print("\n===Test Case #37===")
print("""
Explain basis transformation
""")
input_text = """
Explain basis transformation
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A change of basis consists of converting every assertion expressed in terms of coordinates relative to one basis into an assertion in terms of coordinates rlative to the other basis. Such a conversion results form the change of basis formulat which expresses the coordinated reliave to one basis in terms of coordinates relative to the other basis
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 38
print("\n===Test Case #38===")
print("""
What are eigenheads
""")
input_text = """
What are eigenheads
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Methods of linear algebra are used in the emerging field of
computerized face recognition. Researchers are working with
the idea that every human face in a racial group is a combina-
tion of a few dozen primary shapes. For example, by analyzing
three-dimensional scans of many faces, researchers at Rockefeller
University have produced both an average head shape in the Cau-
casian group—dubbed the meanhead (top row left in the figure
to the left)—and a set of standardized variations from that shape,
called eigenheads (15 of which are shown in the picture). These
are so named because they are eigenvectors of a certain matrix
that stores digitized facial information. Face shapes are repre-
sented mathematically as linear combinations of the eigenheads."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 39
print("\n===Test Case #39===")
print("""
When was eigenvectors made
""")
input_text = """
When was eigenvectors made
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """In the 18th century and early 19th century"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 40
print("\n===Test Case #40===")
print("""
explian invrtibly theorem
""")
input_text = """
explian invrtibly theorem
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A square matrix 𝐴 is invertible if and only if 𝜆 = 0 is not an eigenvalue of 𝐴."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 41
print("\n===Test Case #41===")
print("""
explian invrtibly theorem
""")
input_text = """
explian invrtibly theorem
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A square matrix 𝐴 is invertible if and only if 𝜆 = 0 is not an eigenvalue of 𝐴."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 42
print("\n===Test Case #42===")
print("""
ho made eignvctors
""")
input_text = """
ho made eignvctors
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Leonhard Euler and Augustin-Louis Cauchy"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 43
print("\n===Test Case #43===")
print("""
who made eignvectors in the 18th century?
""")
input_text = """
who made eignvectors in the 18th century?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Leonhard Euler and Augustin-Louis Cauchy"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 44
print("\n===Test Case #44===")
print("""
slv A [
3 0
8 -1
]
""")
input_text = """
slv A [
3 0
8 -1
]
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """It follows from Formula (1) that the eigenvalues of 𝐴 are the solutions of the
equation det(𝜆 𝐼 − 𝐴) = 0, which we can write as
𝜆 − 3 0
−8 𝜆 + 1
= 0
from which we obtain
(𝜆 − 3)(𝜆 + 1) = 0 (2)
This shows that the eigenvalues of 𝐴 are 𝜆 = 3 and 𝜆 = −1. Thus, in addition to the eigen-
value 𝜆 = 3 noted in Example 1, we have discovered a second eigenvalue 𝜆 = −1"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")






#Test Case 45
print("\n===Test Case #45===")
print("What is the formal definition of linear independence?\n")
input_text = "What is the formal definition of linear independence?"
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
#el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/mtvText"]')
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = """If 𝑆 = {v1, v2, . . . , vr} is a set of two or more vectors in a vector space 𝑉,
then 𝑆 is said to be a linearly independent set if no vector in 𝑆 can be expressed as a linear combination of the others.
A set that is not linearly independent is said to be linearly dependent. If 𝑆 has only one vector, we will agree that it
is linearly independent if, and only if that vector is nonzero
"""
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 46
print("\n===Test Case #46===")
print("Who created linear independence?\n")
input_text = "Who created linear independence?"
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = "The concept cannot be attributed to a single person"
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 47
print("\n===Test Case #47===")
print("""Tell me a joke
Is this matrix linearly independent: [(1, 1), (20, 1)]?""")
input_text = """Tell me a joke
Is this matrix linearly independent: [(1, 1), (20, 1)]?"""
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = "Linearly Independent"
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 48
print("\n===Test Case #48===")
print("""Is this matrix: [] linear independent?
""")
input_text = """Is this matrix: [] linear independent?"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "Cannot be determined"

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 49
print("\n===Test Case #49===")
print("""Tell me a joke
When was linear independence made?
""")
input_text = """Tell me a joke
When was linear independence made?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "Unknown"

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 50
print("\n===Test Case #50===")
print("""What is the formal definition of linear independence?
""")
input_text = """What is the formal definition of linear independence?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "A set of vectors {v1,v2,…,vk} is linearly independent if the vector equation x1v1+x2v2+⋯+xkvk=0 has only the trivial solution x1=x2=⋯=xk=0 . The set {v1,v2,…,vk} is linearly dependent otherwise."

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 51
print("\n===Test Case #51===")
print("""Independent linear matrix is: [(5, 500), (250, 15)]?
""")
input_text = """Independent linear matrix is: [(5, 500), (250, 15)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 51
print("\n===Test Case #51===")
print("""Was what Wronskian?
""")
input_text = """Was what Wronskian?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(15)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """If f1 = 𝑓1(x), f2 = 𝑓2(x), . . . , fn = 𝑓n(x) are functions that are n − 1 times differen-
tiable on the interval (−∞, ∞), then the determinant
𝑊(x) =
𝑓1(x) 𝑓2(x) ⋅ ⋅ ⋅ 𝑓n(x)
𝑓′
1 (x) 𝑓′
2 (x) ⋅ ⋅ ⋅ 𝑓′
n (x)
𝑓(n−1)
1 (x) 𝑓(n−1)
2 (x) ⋅ ⋅ ⋅ 𝑓(n−1)
n (x)
is called the Wronskian of 𝑓1, 𝑓2, . . . , 𝑓n."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 52
print("\n===Test Case #52===")
print("""Homogeneous Trivial Solution Theorem is for Linear Independence?
""")
input_text = """Homogeneous Trivial Solution Theorem is for Linear Independence?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 53
print("\n===Test Case #53===")
print("""Independent linear matrix is: [(1, 2), (2, 4)]?
""")
input_text = """Independent linear matrix is: [(1, 2), (2, 4)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Dependent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 54
print("\n===Test Case #54===")
print("""Independent is matrix linear: [(10, 20, 40), (40, 10, 20), (50, 30, 10)]?
""")
input_text = """Independent is matrix linear: [(10, 20, 40), (40, 10, 20), (50, 30, 10)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 55
print("\n===Test Case #55===")
print("""Independence Created of Linear
""")
input_text = """Independence Created of Linear
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """The concept cannot be attributed to a single person"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 56
print("\n===Test Case #56===")
print("""Tell me a joke
Linear is :[(10, 20, 40), (40, 10, 20), (50, 30, 10)] matrix independent?

""")
input_text = """Tell me a joke
Linear is :[(10, 20, 40), (40, 10, 20), (50, 30, 10)] matrix independent?

"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 57
print("\n===Test Case #57===")
print("""Tell me a joke
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """Tell me a joke
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 58
print("\n===Test Case #58===")
print("""Tell me a joke
Theorem Solution Homogeneou Trivial were what
""")
input_text = """Tell me a joke
Theorem Solution Homogeneou Trivial were what
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 59
print("\n===Test Case #59===")
print("""What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 60
print("\n===Test Case #60===")
print("""What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")





#Test Case 61
print("\n===Test Case #61===")
print("""
Who came up with Cramers rule?
""")
input_text = """
Who came up with Cramers rule?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Gaberil Cramer Came up with Cramer's rule"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 62
print("\n===Test Case #62===")
print("""
What is cramers rule?
""")
input_text = """
What is cramers rule?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cramer's Rule is a method of solving systems of linear equations by dividing the values of two determinants.
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 63
print("\n===Test Case #63===")
print("""
solve this matrix with cramers rule []
""")
input_text = """
solve this matrix with cramers rule []
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cramers rule cannot be used to solve it
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 64
print("\n===Test Case #64===")
print("""
What are the limitations to cramers rule
""")
input_text = """
What are the limitations to cramers rule
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cramers rule only works if det(a) does not equal 0, and cramer's rule is slow
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 65
print("\n===Test Case #65===")
print("""
When was cramers rule made?
""")
input_text = """
When was cramers rule made?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """It was founded in the 1750s
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 66
print("\n===Test Case #66===")
print("""Independent linear matrix is: [(1, 2), (2, 4)]?
""")
input_text = """Independent linear matrix is: [(1, 2), (2, 4)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Dependent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 67
print("\n===Test Case #67===")
print("""Independent is matrix linear: [(10, 20, 40), (40, 10, 20), (50, 30, 10)]?
""")
input_text = """Independent is matrix linear: [(10, 20, 40), (40, 10, 20), (50, 30, 10)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 68
print("\n===Test Case #68===")
print("""Independence Created of Linear
""")
input_text = """Independence Created of Linear
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """The concept cannot be attributed to a single person"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 69
print("\n===Test Case #69===")
print("""Tell me a joke
Linear is :[(10, 20, 40), (40, 10, 20), (50, 30, 10)] matrix independent?

""")
input_text = """Tell me a joke
Linear is :[(10, 20, 40), (40, 10, 20), (50, 30, 10)] matrix independent?

"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 70
print("\n===Test Case #70===")
print("""Tell me a joke
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """Tell me a joke
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 71
print("\n===Test Case #71===")
print("""Tell me a joke
Theorem Solution Homogeneou Trivial were what
""")
input_text = """Tell me a joke
Theorem Solution Homogeneou Trivial were what
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 72
print("\n===Test Case #72===")
print("""What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 73
print("\n===Test Case #73===")
print("""Tell me a joke
Linear is :[(-1, -2, -1), (1, 2, 1), (2, 4, 2)] matrix independent?
""")
input_text = """Tell me a joke
Linear is :[(-1, -2, -1), (1, 2, 1), (2, 4, 2)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 74
print("\n===Test Case #74===")
print("""Tell me a joke
Linear is :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] matrix independent?
""")
input_text = """Tell me a joke
Linear is :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 75
print("\n===Test Case #75===")
print("""Tell me a joke
Independence Linear made when?
""")
input_text = """Tell me a joke
Independence Linear made when?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Unknown"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 76
print("\n===Test Case #76===")
print("""Linr si :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] mtxx indiepeendan?
""")
input_text = """Linr si :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] mtxx indiepeendan?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#


#Test Case 77
print("\n===Test Case #77===")
print("""Si tis lnrly indpt -1, -2, -1), (1, 2, 1)2, 4, 2)]?
""")
input_text = """Si tis lnrly indpt -1, -2, -1), (1, 2, 1)2, 4, 2)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 78
print("\n===Test Case #78===")
print("""Linr si :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] mtxx indiepeendan?
""")
input_text = """Linr si :[(-0.2, 0.5, 1.2), (2.3, -1.1, 0.7), (0.8, -0.4, 0.9)] mtxx indiepeendan?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 79
print("\n===Test Case #79===")
print("""Wat is Wonskan?
""")
input_text = """Wat is Wonskan?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """If f1 = 𝑓1(x), f2 = 𝑓2(x), . . . , fn = 𝑓n(x) are functions that are n − 1 times differen-
tiable on the interval (−∞, ∞), then the determinant
𝑊(x) =
𝑓1(x) 𝑓2(x) ⋅ ⋅ ⋅ 𝑓n(x)
𝑓′
1 (x) 𝑓′
2 (x) ⋅ ⋅ ⋅ 𝑓′
n (x)
𝑓(n−1)
1 (x) 𝑓(n−1)
2 (x) ⋅ ⋅ ⋅ 𝑓(n−1)
n (x)
is called the Wronskian of 𝑓1, 𝑓2, . . . , 𝑓n.
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 80
print("\n===Test Case #80===")
print("""sI tis matrick: [] leanare indeependit?
""")
input_text = """sI tis matrick: [] leanare indeependit?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cannot be determined
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 81
print("\n===Test Case #81===")
print("""sI tis matrick: [] leanare indeependit?
""")
input_text = """Matrick sI tis: [] indeependit leanare ?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cannot be determined
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 82
print("\n===Test Case #82===")
print("""Hoo is Crater of Indeependthis Leanher?
""")
input_text = """Hoo is Crater of Indeependthis Leanher?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """The concept cannot be attributed to a single person
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 83
print("\n===Test Case #83===")
print("""Homogeneus triveel soulootion therem ish wat?
""")
input_text = """Homogeneus triveel soulootion therem ish wat?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 84
print("\n===Test Case #84===")
print("""Mayrix solf tis: []
""")
input_text = """Mayrix solf tis: []
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cannot be determined"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 85
print("\n===Test Case #85===")
print("""Is leaner indiependence formal deafinition?
""")
input_text = """Is leaner indiependence formal deafinition?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """If 𝑆 = {v1, v2, . . . , vr} is a set of two or more vectors in a vector space 𝑉,
then 𝑆 is said to be a linearly independent set if no vector in 𝑆 can be expressed as a linear combination of the others.
A set that is not linearly independent is said to be linearly dependent. If 𝑆 has only one vector, we will agree that it
is linearly independent if, and only if that vector is nonzero
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 86
print("\n===Test Case #86===")
print("""Mayduh leaner indiependant whun?
""")
input_text = """Mayduh leaner indiependant whun?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Unknown
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 87
print("\n===Test Case #87===")
print("""explain invertibility theorem linear algebra
""")
input_text = """explain invertibility theorem linear algebra
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """a square matrix a is invertible if and only if lambda = 0 is not an eigenvalue of A
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 88
print("\n===Test Case #88===")
print("""who made eigenvectors
""")
input_text = """who made eigenvectors
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Leonhard Euler
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 89
print("\n===Test Case #89===")
print("""
In Example 1 we observed that 𝜆 = 3 is an eigenvalue of the matrix
𝐴 = [3 0
8 −1]
but we did not explain how we found it. Use the characteristic equation to find all eigenvalues
of this matrix.
""")
input_text = """
In Example 1 we observed that 𝜆 = 3 is an eigenvalue of the matrix
𝐴 = [3 0
8 −1]
but we did not explain how we found it. Use the characteristic equation to find all eigenvalues
of this matrix.
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """This shows that the eigenvalues of 𝐴 are 𝜆 = 3 and 𝜆 = −1. Thus, in addition to the eigen-
value 𝜆 = 3 noted in Example 1, we have discovered a second eigenvalue 𝜆 = −1.
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 90
print("\n===Test Case #90===")
print("""
Find the eigenvalues of
𝐴 = [
0 1 0
0 0 1
4 −17 8
""")
input_text = """
Find the eigenvalues of
𝐴 = [
0 1 0
0 0 1
4 −17 8
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Thus, the eigenvalues of 𝐴 are
𝜆 = 4, 𝜆 = 2 + √3, and 𝜆 = 2 − √3
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 91
print("\n===Test Case #91===")
print("""
Find the eigenvalues of this 0x0 matrix
""")
input_text = """
Find the eigenvalues of this 0x0 matrix
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """eigenvalue of 0 and all non-zero vectors as your eigenvectors
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 92
print("\n===Test Case #92===")
print("""
Explain eigenspaces
""")
input_text = """
Explain eigenspaces
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Now that we know how to find the eigenvalues of a matrix, we will consider the problem of
finding the corresponding eigenvectors. By definition, the eigenvectors of 𝐴 correspond-
ing to an eigenvalue 𝜆 are the nonzero vectors that satisfy
(𝜆𝐼 − 𝐴) x = 0
Thus, we can find the eigenvectors of 𝐴 corresponding to 𝜆 by finding the nonzero vec-
tors in the solution space of this linear system. This solution space, which is called the
eigenspace of 𝐴 corresponding to 𝜆, can also be viewed as:
1. the null space of the matrix 𝜆𝐼 − 𝐴
2. the kernel of the matrix operator 𝑇𝜆 𝐼−𝐴∶ 𝑅n → 𝑅n
3. the set of vectors for which 𝐴x = 𝜆x
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 93
print("\n===Test Case #93===")
print("""
Explain basis transformation
""")
input_text = """
Explain basis transformation
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A change of basis consists of converting every assertion expressed in terms of coordinates relative to one basis into an assertion in terms of coordinates rlative to the other basis. Such a conversion results form the change of basis formulat which expresses the coordinated reliave to one basis in terms of coordinates relative to the other basis
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 94
print("\n===Test Case #94===")
print("""
What are eigenheads
""")
input_text = """
What are eigenheads
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Methods of linear algebra are used in the emerging field of
computerized face recognition. Researchers are working with
the idea that every human face in a racial group is a combina-
tion of a few dozen primary shapes. For example, by analyzing
three-dimensional scans of many faces, researchers at Rockefeller
University have produced both an average head shape in the Cau-
casian group—dubbed the meanhead (top row left in the figure
to the left)—and a set of standardized variations from that shape,
called eigenheads (15 of which are shown in the picture). These
are so named because they are eigenvectors of a certain matrix
that stores digitized facial information. Face shapes are repre-
sented mathematically as linear combinations of the eigenheads."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 95
print("\n===Test Case #95===")
print("""
When was eigenvectors made
""")
input_text = """
When was eigenvectors made
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """In the 18th century and early 19th century"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 96
print("\n===Test Case #96===")
print("""
explian invrtibly theorem
""")
input_text = """
explian invrtibly theorem
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A square matrix 𝐴 is invertible if and only if 𝜆 = 0 is not an eigenvalue of 𝐴."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 97
print("\n===Test Case #97===")
print("""
explian invrtibly theorem
""")
input_text = """
explian invrtibly theorem
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A square matrix 𝐴 is invertible if and only if 𝜆 = 0 is not an eigenvalue of 𝐴."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 98
print("\n===Test Case #98===")
print("""
ho made eignvctors
""")
input_text = """
ho made eignvctors
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Leonhard Euler and Augustin-Louis Cauchy"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 99
print("\n===Test Case #99===")
print("""
who made eignvectors in the 18th century?
""")
input_text = """
who made eignvectors in the 18th century?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Leonhard Euler and Augustin-Louis Cauchy"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 100
print("\n===Test Case #100===")
print("""
slv A [
3 0
8 -1
]
""")
input_text = """
slv A [
3 0
8 -1
]
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """It follows from Formula (1) that the eigenvalues of 𝐴 are the solutions of the
equation det(𝜆 𝐼 − 𝐴) = 0, which we can write as
𝜆 − 3 0
−8 𝜆 + 1
= 0
from which we obtain
(𝜆 − 3)(𝜆 + 1) = 0 (2)
This shows that the eigenvalues of 𝐴 are 𝜆 = 3 and 𝜆 = −1. Thus, in addition to the eigen-
value 𝜆 = 3 noted in Example 1, we have discovered a second eigenvalue 𝜆 = −1"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")






#Test Case 101
print("\n===Test Case #101===")
print("What is the formal definition of linear independence?\n")
input_text = "What is the formal definition of linear independence?"
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
#el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/mtvText"]')
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = """If 𝑆 = {v1, v2, . . . , vr} is a set of two or more vectors in a vector space 𝑉,
then 𝑆 is said to be a linearly independent set if no vector in 𝑆 can be expressed as a linear combination of the others.
A set that is not linearly independent is said to be linearly dependent. If 𝑆 has only one vector, we will agree that it
is linearly independent if, and only if that vector is nonzero
"""
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 102
print("\n===Test Case #102===")
print("Who created linear independence?\n")
input_text = "Who created linear independence?"
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = "The concept cannot be attributed to a single person"
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 103
print("\n===Test Case #103===")
print("""Tell me a joke
Is this matrix linearly independent: [(1, 1), (20, 1)]?""")
input_text = """Tell me a joke
Is this matrix linearly independent: [(1, 1), (20, 1)]?"""
el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text
actual_answer = "Linearly Independent"
doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 104
print("\n===Test Case #104===")
print("""Is this matrix: [] linear independent?
""")
input_text = """Is this matrix: [] linear independent?"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "Cannot be determined"

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")

#Test Case 105
print("\n===Test Case #105===")
print("""Tell me a joke
When was linear independence made?
""")
input_text = """Tell me a joke
When was linear independence made?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "Unknown"

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 106
print("\n===Test Case #106===")
print("""What is the formal definition of linear independence?
""")
input_text = """What is the formal definition of linear independence?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = "A set of vectors {v1,v2,…,vk} is linearly independent if the vector equation x1v1+x2v2+⋯+xkvk=0 has only the trivial solution x1=x2=⋯=xk=0 . The set {v1,v2,…,vk} is linearly dependent otherwise."

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 107
print("\n===Test Case #107===")
print("""Independent linear matrix is: [(5, 500), (250, 15)]?
""")
input_text = """Independent linear matrix is: [(5, 500), (250, 15)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 108
print("\n===Test Case #108===")
print("""Was what Wronskian?
""")
input_text = """Was what Wronskian?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(15)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """If f1 = 𝑓1(x), f2 = 𝑓2(x), . . . , fn = 𝑓n(x) are functions that are n − 1 times differen-
tiable on the interval (−∞, ∞), then the determinant
𝑊(x) =
𝑓1(x) 𝑓2(x) ⋅ ⋅ ⋅ 𝑓n(x)
𝑓′
1 (x) 𝑓′
2 (x) ⋅ ⋅ ⋅ 𝑓′
n (x)
𝑓(n−1)
1 (x) 𝑓(n−1)
2 (x) ⋅ ⋅ ⋅ 𝑓(n−1)
n (x)
is called the Wronskian of 𝑓1, 𝑓2, . . . , 𝑓n."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 109
print("\n===Test Case #109===")
print("""Homogeneous Trivial Solution Theorem is for Linear Independence?
""")
input_text = """Homogeneous Trivial Solution Theorem is for Linear Independence?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 110
print("\n===Test Case #110===")
print("""Independent linear matrix is: [(1, 2), (2, 4)]?
""")
input_text = """Independent linear matrix is: [(1, 2), (2, 4)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Dependent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 111
print("\n===Test Case #111===")
print("""Independent is matrix linear: [(10, 20, 40), (40, 10, 20), (50, 30, 10)]?
""")
input_text = """Independent is matrix linear: [(10, 20, 40), (40, 10, 20), (50, 30, 10)]?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 112
print("\n===Test Case #112===")
print("""Independence Created of Linear
""")
input_text = """Independence Created of Linear
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """The concept cannot be attributed to a single person"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")
#

#Test Case 113
print("\n===Test Case #113===")
print("""Tell me a joke
Linear is :[(10, 20, 40), (40, 10, 20), (50, 30, 10)] matrix independent?

""")
input_text = """Tell me a joke
Linear is :[(10, 20, 40), (40, 10, 20), (50, 30, 10)] matrix independent?

"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 114
print("\n===Test Case #114===")
print("""Tell me a joke
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """Tell me a joke
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 115
print("\n===Test Case #115===")
print("""Tell me a joke
Theorem Solution Homogeneou Trivial were what
""")
input_text = """Tell me a joke
Theorem Solution Homogeneou Trivial were what
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """A nonempty set 𝑆 = {v1, v2, . . . , vr} in a vector space 𝑉 is linearly independent if
and only if the only coefficients satisfying the vector equation
k1v1 + k2v2 + ⋅ ⋅ ⋅ + krvr = 0
are k1 = 0, k2 = 0, . . . , kr = 0."""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")



#Test Case 116
print("\n===Test Case #116===")
print("""What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 117
print("\n===Test Case #117===")
print("""What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
""")
input_text = """What is the weight of the world
Linear is :[(-123, -533, 42), (1, 5, -3), (3, 3, 1)] matrix independent?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Linearly Independent"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")





#Test Case 118
print("\n===Test Case #118===")
print("""
Who came up with Cramers rule?
""")
input_text = """
Who came up with Cramers rule?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Gaberil Cramer Came up with Cramer's rule"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 119
print("\n===Test Case #119===")
print("""
What is cramers rule?
""")
input_text = """
What is cramers rule?
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[4]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cramer's Rule is a method of solving systems of linear equations by dividing the values of two determinants.
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


#Test Case 120
print("\n===Test Case #120===")
print("""
solve this matrix with cramers rule []
""")
input_text = """
solve this matrix with cramers rule []
"""

el = driver.find_element(AppiumBy.XPATH, '//*[@text="Message"]').send_keys(input_text)
el = driver.find_element(AppiumBy.XPATH, '//*[@resource-id="com.scaleup.chatai:id/ivSent"]').click()
time.sleep(10)
el = driver.find_element(AppiumBy.XPATH, '//androidx.recyclerview.widget.RecyclerView[@resource-id="com.scaleup.chatai:id/rvConversation"]/android.view.ViewGroup[2]/android.widget.TextView[@resource-id="com.scaleup.chatai:id/mtvText"]')
result_text = el.text

actual_answer = """Cramers rule cannot be used to solve it
"""

doc1 = nlp(actual_answer)
doc2 = nlp(result_text)
print("Chatbot Response: ", result_text)
print("Expected Response: ", actual_answer)
print("Similarity Score: ", doc1.similarity(doc2))
print("Test Case Result: ", get_score(doc1.similarity(doc2)), "\n")


time.sleep(10)
