# Local Model
## Install

[](https://github.com/lucidrains/DALLE-pytorch#install)
```python
$ pip install dalle-pytorch
```
We trained the model using a dataset with fashion items. We trained it with the following parameters:
epochs: 30, batch_size: 5, learning_rate: 4.5e-4, depth: 16, heads: 12, head_dimension: 64.
For our trainings we used 2 GPUs ...
 
The fashion dataset we used can be downloaded from this [Kaggle link](https://www.kaggle.com/datasets/paramaggarwal/fashion-product-images-dataset)
**common_words.txt:** Is a list with the most commonly found words in the descriptions. They were found using  **find_common_words.py**
**examples:** Contains folders with some of the local generations.
**outputs:** There will be saved all the generations you will make.
**fashion_16_12_30ep.pt:** Is the model we trained to generate fashion items.
*(To access the model contact : teoaivalis@iit.demokritos.gr )*
**train_dalle.py:** Is the file you use to train your own model.
**generate.py:** Is the file you use to generate images with your own prompts.
**config.yaml:** Configuration file to train dalle-pytorch.
**config1.yaml:** Configuration file to retrain dalle-pytorch for unlearning.


# Struct of the Code
<style>
/* Styles for folder icons */
.folder-icon {
    color: #007bff; /* Blue color for folder icons */
    font-size: 24px; /* Adjust size as needed */
    margin-right: 8px; /* Add space between icon and text */
}

/* Styles for file icons */
.file-icon {
    color: #28a745; /* Green color for file icons */
    font-size: 20px; /* Adjust size as needed */
    margin-right: 8px; /* Add space between icon and text */
}

/* Styles for folder names */
.folder-name {
    font-weight: bold; /* Make folder names bold */
}

/* Styles for file names */
.file-name {
    /* No specific styles for file names */
}

/* Styles for comments */
.file-comment {
    font-style: italic; /* Make comments italic */
    color: #6c757d; /* Gray color for comments */
}
</style>

<!-- Folder structure -->
<ul>
    <li>
        <span class="folder-icon">&#128193;</span> <!-- Unicode for folder icon -->
        <span class="folder-name">Local_Dalle</span>
        <ul>
            <li>
                <span class="folder-icon">&#128193;</span>
                <span class="folder-name">images</span>
                <ul>
                    <li><span class="file-icon">&#128196;</span>
                        <span class="file-name">fashion_items.zip</span> <!-- Fashion dataset -->
                    </li>
                    <li><span class="file-icon">&#128196;</span>
                        <span class="file-name">decrease_txt_files.py</span> <!-- Keep only certain lines of the descriptions training files -->
                    </li>
                    <li><span class="file-icon">&#128196;</span>
                        <span class="file-name">find_common_words.py</span> <!-- Finds the most common words included in the descriptions of the dataset -->
                    </li>
                    <li><span class="file-icon">&#128196;</span>
                        <span class="file-name">common_words.txt</span> <!-- Most common words in the descriptions -->
                    </li>
                </ul>
            </li>
            <li>
                <span class="folder-icon">&#128193;</span>
                <span class="folder-name">examples</span>
            </li>
            <li>
                <span class="folder-icon">&#128193;</span>
                <span class="folder-name">outputs</span> <!-- Examples of the local generations -->
            </li>
            <li><span class="file-icon">&#128196;</span>
                <span class="file-name">fashion_16_12_30ep.pt</span>
            </li>
            <li><span class="file-icon">&#128196;</span>
                <span class="file-name">train_dalle.py</span>
            </li>
            <li><span class="file-icon">&#128196;</span>
                <span class="file-name">train_vae.py</span>
           </li>
           <li><span class="file-icon">&#128196;</span>
                <span class="file-name">generate.py</span>
           </li>
            <li><span class="file-icon">&#128196;</span>
                <span class="file-name">config.yaml</span> <!-- Configuration file to train dalle-pytorch -->
            </li>
            <li><span class="file-icon">&#128196;</span>
                <span class="file-name">config1.yaml</span> <!-- Configuration file to retrain dalle-pytorch for unlearning -->
            </li>
        </ul>
    </li>
    </ul>
