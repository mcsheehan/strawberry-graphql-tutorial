from typing import Dict, List, Optional

from gql import gql, Client
from gql.transport.requests import RequestsHTTPTransport

# Select your transport with a defined url endpoint

url = 'http://0.0.0.0:8000/graphql'
headers = {}

transport = RequestsHTTPTransport(url=url, headers=headers)

# Create a GraphQL client using the defined transport
client = Client(transport=transport, fetch_schema_from_transport=False)

def get_book_by_id(book_title: str) -> Optional[Dict]:
    # Provide a GraphQL query
    query = gql(
        """
        query BookQuery($bookTitle: String!) {
          getBookByTitle(bookTitle: $bookTitle) {
            author
            title
          }
        }
        """
    )

    result = client.execute(query, variable_values={"bookTitle": book_title})
    return result["getBookByTitle"]


if __name__ == '__main__':
    lovely_book = get_book_by_id("a book about bottoms")
    print(lovely_book)
