<!-- # AIOps-project-DVC-NLP-uscase
AIOps project DVC-NLP-uscase -->

![AIOps-project-DVC-NLP-usecase](https://socialify.git.ci/c17hawke/AIOps-project-DVC-NLP-usecase/image?forks=1&issues=1&language=1&name=1&owner=1&pattern=Circuit%20Board&pulls=1&stargazers=1&theme=Dark)

* data is available at - [this googele drive link](https://drive.google.com/file/d/13A0RtvZZanHXKZNbz5JKwjjO2FedNQCR/view?usp=sharing)

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
