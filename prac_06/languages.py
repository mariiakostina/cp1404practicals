"""
Estimated time: 10 min
Actual time: 23:32 started, 17 min
"""

from prac_06.programming_language import ProgrammingLanguage

def main():
    """Demo the use of ProgrammingLanguage class"""
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

    languages = [python, ruby, visual_basic]

    print("The dynamically typed languages are:")
    for language in languages:
        if language.is_dynamic():
            print(language.name)

if __name__ == "__main__":
    main()

