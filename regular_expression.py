import re

text1 = """
    Lorem ipsum dolor sit amet, consectetuer adipiscing elit. Aenean commodo ligula eget dolor. Aenean massa. Cum sociis natoque penatibus et magnis dis parturient montes, nascetur ridiculus mus. 9943300303 Tesla's CFO number (999)-333-7777
"""

pattern = r'\(\d{3}\)-\d{3}-\d{4}|\d{10}'

matches = re.findall(pattern, text1)
print(matches)


text2 = """Note 1 - Summary of Significant Accounting Policies
Unaudited Interim Financial Statements
The consolidated financial statements of Tesla, Inc. (“Tesla”, the “Company”, “we”, “us” or “our”), including the consolidated balance sheet as of September 30, 2025, the consolidated statements of operations, the consolidated statements of comprehensive income, the consolidated statements of redeemable noncontrolling interests and equity for the three and nine months ended September 30, 2025 and 2024, and the consolidated statements of cash flows for the nine months ended September 30, 2025 and 2024, as well as other information disclosed in the accompanying notes, are unaudited. The consolidated balance sheet as of December 31, 2024.
Note 2 - Fair Value of Financial Instruments
ASC 820, Fair Value Measurements states that fair value is an exit price, representing the amount that would be received to sell an asset or paid to transfer a liability in an orderly transaction between market participants.
Note 3 - Inventory
Our inventory consisted of the following (in millions)."""

pattern = r'Note \d - ([^\n]*)'
print(re.findall(pattern, text2))

text3 = """The gross cost of automotive leasing revenue in FY2026 Q1 was $0.196 billion. In the previous quarter, i.e., FY2025 Q4, it was $0.206 billion."""

pattern = r'FY(\d{4} Q[1-4])[^\$]+(\$\d+\.\d* \w*)'
print(re.findall(pattern, text3))