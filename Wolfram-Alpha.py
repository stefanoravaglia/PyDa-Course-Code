import wolframclient
import wolframclient as wf

q = input("Q: ")
app_id = "243U9E-72PXGKHT38"
client = wf

#wolframalpha.Client(app_id)


res = client.query(q)
answer = next(res.results).text

print(answer)

