import typer
import feedparser

app = typer.Typer(help="Awesome CLI feed rss.")

@app.command()
def rss(url: str):
    """
        Reader will display the title, description, and link of the original content with : URL
    """
    try:
        d = feedparser.parse(url)
        for i in d.entries:
            print(i.title)
            print(i.links)
            print(i.description)
            max_len = max(len(i.description), len(i.title))
            print("-" * max_len)
    except:
        print("The link may not be valid 🤔")

if __name__ == "__main__":
    app()