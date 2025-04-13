import wikipedia
def main():
    """Search and display Wikipedia page."""
    title = input("Enter page title: ").strip()
    while title != "":
        try:
            page = wikipedia.page(title, auto_suggest=False)  # In some versions autosuggest differently spelled, mine accept auto_suggest
            print(f"{page.title}")
            print(wikipedia.summary(title, sentences=2))
            print(page.url)
        except wikipedia.exceptions.DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except wikipedia.exceptions.PageError:
            print(f'Page id "{title}" does not match any pages. Try another id!')

        title = input("\nEnter page title: ")

    print("Thank you.")

if __name__ == "__main__":
    main()



