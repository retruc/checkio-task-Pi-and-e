"""
TESTS is a dict with all you tests.
Keys for this will be categories' names.
Each test is dict with
    "input" -- input data for user function
    "answer" -- your right answer
    "explanation" -- not necessary key, it's using for additional info in animation.
"""

TESTS = {
    "Basics": [
        {"input": [5.85987448205], "answer": 'e+pi'},
        {"input": [18.2958548951], "answer": 'e**e+pi'},
        {"input": [47.6085189284], "answer": 'e**e*pi'},
        {"input": [-0.42331082513], "answer": 'e-pi'},
        {"input": [7.38905609893], "answer": 'e*e'},

    ],
    "Extra": [
        {"input": [3.14159265359], "answer": 'pi'},
        {"input": [-2.48054830216], "answer": 'e*e-pi*pi'},
        {"input": [57.9087276547], "answer": 'e*pi**e-pi'},
        {"input": [0.07455076325], "answer": 'e/pi**pi'},
        {"input": [2.00000000000], "answer": None},
        {"input": [0.10132118364], "answer": 'e/e/pi/pi'},

    ]
}
