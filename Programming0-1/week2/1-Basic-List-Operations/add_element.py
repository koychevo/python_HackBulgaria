languages = ["Python", "Ruby"]

languages = languages + ["C++"] + ["Java"] + ["C#"]
print(languages)

languages = ["Haskell"] + languages
print(languages)

languages += ["Go"]
print(languages)

print(languages[0])
print(languages[1])
print(languages[5])

languages[5] = "F#"
print(languages)

print(languages[len(languages) - 1])

print("Haskell" in languages)
print("Ruby" in languages)
print("Go" in languages)
print("Rust" in languages)