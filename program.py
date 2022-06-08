## oCsx42uGYOgJcHIzMnhAo3YoqnQWQdjd821QS6xbwr54NhHwyUI0bjBE91H9EbzUvB03QarGtLwYZd010X2ENAqN9HnhFjvSIfXOWYLX6ROZNBDoKvrsxgkqsXMSEDmN
## fuS4q8qbmS0lNHNqhMvbjrySmvZrlJbL7DlC60REUsDsob1QevCwBqrD0gnFACVmOGCPevrACmobkj7Nf3QEjD8gKesqw4A88FY0tPyhkTXB443ZTytKC4QjOmP21Wct
## ClMrnoZ80IE596QTaNL5HG64nhigcokdC8iprN7BMlPfOB5pnLlEs2kQyX27Kl2w6TNTYmVcB0ApiMQHA8nU8v4u2CQKQ2aecD6PfFyDkFddFWGMlG7YoHRyOEexQeYf

# All comments started with ## will be randomized each time it runs
import random

## KMbDuk6bAsYMpZjGtdBtben8QorlHTUFUvlDlhlmX8jgZzdOMt0FpiAwRgBBuUXmAMQi0HvUGcqlwQIyvjNcWCNV9cTtc9YhmF77FrDlQeAL0rrGE5uu7r7PFRETsPCT

# Generate randomized text
def randomtext(le):
    out = ""
    for i in range(le):
        out += random.sample("qwertyuiopasdfghjklzxcvbnm1234567890QWERTYUIOPASDFGHJKLZXCVBNM",1)[0]
    return out


## QfhET6cBHPnWSsd0qUacNZbmOiv71lrDRiiDWUuBOvbYAtVBsvDsmHM9ErWvYbk5cSEETT01Ugy8NDQKiGX2H5Oumkhotpq5SMJ6LwiUt7i19YtR7gHkLqz2CLSWZcXy

# Read the code
code = ""
with open('program.py', 'r') as f:
    code = f.read()

## 4ftRhqt16KH542wqGl4AeFFWIqnNegEAayn5EGDmHJHmWxkYhzx7JF4iIMEEtguP4IKmAEQWdbCL35iS6SJAURetzTlpX9QsdH6g5oqBLjKRRUPOJW2Y3mOfZY6wBsl4

code = code.split('\n')

## rmH3967ICaoeZB1smbp2lTJjHincmahDpaMhAcK2qz9LoWirfE20R1vPdy6M3gjQsOVuYuD3ei13VIdVg61SbLuimWZzfiACbemQburH0Kxxwdy4zZQoRi5RZEhozmqI

# Generate new random comments
for i in range(len(code)):
    if code[i][:2] == '##':
        code[i] = '##' + ' ' + randomtext(128)

## o836efGJibKRhaRG8Q3uAdbnvCbQIt9iH4kb9ZO6JRqqQ2gxEVgJeXtfeAdQz7lZstkAXodO2ilnpP1bA8erDKpuW9B7qwV8AHL45JBgkQx1gaZmEsOdrjzEhoszYkC7

# Save it back
with open('program.py', 'w') as f:
    f.write('\n'.join(code))

print('finished: Run checksum again to check the signature')


## avBtn2GR3u85XHfmdqxUpvgSU8NRoYb1p3xG6NvqMBWYEyP7VPJLYgG11VB3UYT4Lp32dfAebFXNcfsIaySWI3EgvJRQozBor00nFwUzOkUfhcAlt0hcSdh6ErDSYq06
## lf1EbN4zuruOXnSWAyaon2h8YdwWmJnaJTeiF0cFkFVBo0nv4PHaVZz0PoS8E75Tmsb6gJ804Skaa5yjXbqyVzy4URNopEua3HeRF1E7hpMyoBoWdgEDeBXKl0gWvXq3
## iplFq6BVPplg3Hwyth9dziU1OOsvLWhXnUGEwG5tyicfiW223uUl7GkrNPrmNNPfCD9iGX8BfvC7uX6grSgeMpjwJ6RgRJU46yXXgkdbGIYSBWhjg7AXOUxQHdsmhxCG


