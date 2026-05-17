import requests
import sys

def test_process_call(file_path):
    url = "http://localhost:8000/process-call"
    files = {'file': open(file_path, 'rb')}
    response = requests.post(url, files=files)
    print("Process Call Response:")
    print(response.json())

def test_search(query):
    url = f"http://localhost:8000/search?query={query}"
    response = requests.get(url)
    print("\nSearch Response:")
    print(response.json())

if __name__ == "__main__":
    if len(sys.argv) > 1:
        if sys.argv[1] == "process":
            test_process_call(sys.argv[2])
        elif sys.argv[1] == "search":
            test_search(sys.argv[2])
    else:
        print("Uso: python test_api.py process <caminho_audio> ou python test_api.py search <pergunta>")
