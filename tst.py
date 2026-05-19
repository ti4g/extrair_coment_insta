from instagrapi import Client
import csv

cl = Client()
cl.delay_range = [2, 5]
cl.login("xx", "xx")

SHORTCODE = "DW4iWK7CUFi"
media_pk = cl.media_pk_from_code(SHORTCODE)
print(f"Media PK: {media_pk}")
print("Baixando comentários...")

vistos = set()
with open("comentaristas.csv", "w", newline="", encoding="utf-8") as f:
    w = csv.writer(f)
    w.writerow(["username", "comentario", "data", "likes"])
    
    try:
        comentarios = cl.media_comments(media_pk, amount=0)
        for i, c in enumerate(comentarios, 1):
            w.writerow([c.user.username, c.text, c.created_at_utc, c.like_count])
            vistos.add(c.user.username)
            if i % 50 == 0:
                f.flush()
                print(f"  {i} comentários | {len(vistos)} usuários únicos")
    except KeyboardInterrupt:
        print("\nInterrompido. O que baixou já está no CSV.")
    except Exception as e:
        print(f"\nErro: {e}")
        print("O que baixou até aqui está salvo no CSV.")

print(f"\n✅ Total: {len(vistos)} pessoas únicas no arquivo comentaristas.csv")