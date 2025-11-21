# AI Test voor Atsumi - Educatief Platform
from openai import OpenAI

# VUL HIER JE EIGEN API KEY IN
api_key = "plak_hier_jouw_api_key"

client = OpenAI(api_key=api_key)

print("🧩 Atsumi AI Test - Educatief Platform")
print("AI wordt aangeroepen...")

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": "Bedenk een korte, autismevriendelijke educatieve activiteit voor kinderen die helpt met emotieherkenning. Beschrijf het in het Nederlands in maximaal 3 zinnen."}
        ],
        max_tokens=150
    )
    
    print("✅ SUCCES! AI suggestie voor Atsumi:")
    print("=" * 60)
    print(response.choices[0].message.content)
    print("=" * 60)
    print("🎉 Perfect voor je educatieve platform!")
    
except Exception as e:
    print("❌ Fout:", e)
    print("Controleer je API key en internetverbinding")
