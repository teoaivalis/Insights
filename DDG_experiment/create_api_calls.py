import pandas as pd
import pickle

# read specific columns of csv file using Pandas
print("read text prompts")
df_prompts = pd.read_csv("./Insights_from _the_adtaset/DDG_experiment/prompts.csv")
print(df_prompts)
prompts = df_prompts.values.tolist()
print(len(prompts))

print("read image links")
df_images = pd.read_csv("./Insights_from _the_adtaset/DDG_experiment/image_list.csv")
print(df_images)
images = df_images.values.tolist()
print(len(images))

substring = "https://"
link = 0
valid = 0
invalid = 0
ch = 0
with open('./Insights_from _the_adtaset/DDG_experiment/api_calls.sh', 'w') as f:
    for i in range (len(prompts)):
        st = ''.join(prompts[i])
        if substring in st:
            link += 1
        else:
          if (contains_chinese(str(st))):
            if len(str(st)) < 170:
              ch = ch + 1
              f.write("ddgs images -k '")
              y = prompts[i]
              z = y[0].replace("'", "")
              f.write(z)
              f.write("' -m 10 -s off -d -r ch-zh \n")
              f.write("cd $(ls -t | head -n 1)\n")
              f.write("touch prompt.txt\n")
              f.write(f'echo "{st}" >> prompt.txt\n')
              f.write("touch help.py\n")
              f.write("echo 'import requests' >> help.py\n")
              f.write(f"echo 'url = \"{im[0]}\"' >> help.py\n")
              f.write(f'echo "try:" >> help.py\n')
              f.write(f'echo "    response = requests.get(url, stream=True, allow_redirects=False, timeout=5)" >> help.py\n')
              f.write(f'echo "except requests.exceptions.ReadTimeout:" >> help.py\n')
              f.write(f'echo "    pass" >> help.py\n')
              f.write(f'echo "with open(\\"gen_image.png\\", \\"wb\\") as f:" >> help.py\n')
              f.write(f'echo "    f.write(response.content)" >> help.py\n')
              f.write("python3 help.py\n")
              f.write("cd ..\n")
            else :
              z = prompts[i]
              x = z[0].replace("'", "")
              y = []
              y.append(x)
              simplified_sentences = simplify_sentences(y)
              f.write("ddgs images -k '")
              f.write(simplified_sentences[0])
              f.write("' -m 10 -s off -d -r ch-zh \n")
              f.write("cd $(ls -t | head -n 1)\n")
              f.write("touch prompt.txt\n")
              f.write(f'echo "{st}" >> prompt.txt\n')
              f.write("touch help.py\n")
              f.write("echo 'import requests' >> help.py\n")
              f.write(f"echo 'url = \"{im[0]}\"' >> help.py\n")
              f.write(f'echo "try:" >> help.py\n')
              f.write(f'echo "    response = requests.get(url, stream=True, allow_redirects=False, timeout=5)" >> help.py\n')
              f.write(f'echo "except requests.exceptions.ReadTimeout:" >> help.py\n')
              f.write(f'echo "    pass" >> help.py\n')
              f.write(f'echo "with open(\\"gen_image.png\\", \\"wb\\") as f:" >> help.py\n')
              f.write(f'echo "    f.write(response.content)" >> help.py\n')
              f.write("python3 help.py\n")
              f.write("cd ..\n")
          else:
            im = images[i]
            if len(str(st)) < 170:
                valid += 1
                f.write("ddgs images -k '")
                y = prompts[i]
                z = y[0].replace("'", "")
                f.write(z)
                f.write("' -m 10 -s off -d \n")
                f.write("cd $(ls -t | head -n 1)\n")
                f.write("touch prompt.txt\n")
                f.write(f'echo "{st}" >> prompt.txt\n')
                f.write("touch help.py\n")
                f.write("echo 'import requests' >> help.py\n")
                f.write(f"echo 'url = \"{im[0]}\"' >> help.py\n")
                f.write(f'echo "try:" >> help.py\n')
                f.write(f'echo "    response = requests.get(url, stream=True, allow_redirects=False, timeout=5)" >> help.py\n')
                f.write(f'echo "except requests.exceptions.ReadTimeout:" >> help.py\n')
                f.write(f'echo "    pass" >> help.py\n')
                f.write(f'echo "with open(\\"gen_image.png\\", \\"wb\\") as f:" >> help.py\n')
                f.write(f'echo "    f.write(response.content)" >> help.py\n')
                f.write("python3 help.py\n")
                f.write("cd ..\n")
            else:
                invalid += 1
                z = prompts[i]
                x = z[0].replace("'", "")
                y = []
                y.append(x)
                simplified_sentences = simplify_sentences(y)
                f.write("ddgs images -k '")
                f.write(simplified_sentences[0])
                f.write("' -m 10 -s off -d \n")
                f.write("cd $(ls -t | head -n 1)\n")
                f.write("touch prompt.txt\n")
                f.write(f'echo "{st}" >> prompt.txt\n')
                f.write("touch help.py\n")
                f.write("echo 'import requests' >> help.py\n")
                f.write(f"echo 'url = \"{im[0]}\"' >> help.py\n")
                f.write(f'echo "try:" >> help.py\n')
                f.write(f'echo "    response = requests.get(url, stream=True, allow_redirects=False, timeout=5)" >> help.py\n')
                f.write(f'echo "except requests.exceptions.ReadTimeout:" >> help.py\n')
                f.write(f'echo "    pass" >> help.py\n')
                f.write(f'echo "with open(\\"gen_image.png\\", \\"wb\\") as f:" >> help.py\n')
                f.write(f'echo "    f.write(response.content)" >> help.py\n')
                f.write("python3 help.py\n")
                f.write("cd ..\n")
