import gdown
import aspose.zip as az

url = ("https://drive.google.com/file/d/1Yd0WxHgkNgEQDLCXpIf3CiqVVZB8495i/view?usp=sharing")
output = "datasets.rar"
gdown.download(url=url, output=output, fuzzy=True)

with az.rar.RarArchive("datasets.rar") as archive:
    archive.extract_to_directory("./")
