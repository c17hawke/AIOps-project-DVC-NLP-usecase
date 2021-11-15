# AIOps-project-DVC-NLP-uscase
AIOps project DVC-NLP-uscase

## Important References - 

* [Bag of Words- Krish Naik](https://youtu.be/D2V1okCEsiE)

* [TF-IDF- Krish Naik](https://youtu.be/D2V1okCEsiE)

* [DVC studio home page](https://studio.iterative.ai/)
## STEPS -

### STEP 01- Create a repository by using template repository

### STEP 02- Clone the new repository

### STEP 03- Create a conda environment after opening the repository in VSCODE

```bash
conda create --prefix ./env python=3.7 -y
```

```bash
conda activate ./env
```
OR
```bash
source activate ./env
```

### STEP 04- install the requirements
```bash
pip install -r requirements.txt
```

### STEP 05- initialize the dvc project
```bash
dvc init
```

### STEP 06- commit and push the changes to the remote repository