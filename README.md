# Insights from the Dataset
**Abstract:** Generative AI models are experiencing rapid development across various aspects of people's life. However, there are significant ethical and social concerns. These oppositions primarily arise from artists and content creators whose works is used for training these AI models. These concerns arise from the black-box nature of these models, characterized by their large number of parameters and complexity, making it challenging to understand how they operate and the potential impacts of their outputs.
Our paper approaches these concerns by introducing a method capable of extracting influential subsets from the training dataset. Our methodology focuses on enhancing the Interpretability of generative models by analyzing connections between training data and model's outputs. 


# Train a generative model locally:
In order to train and use a local model for our generations we used the [Dalle-pytorch](https://github.com/lucidrains/DALLE-pytorch) package. It is an implementation of [DALL-E](https://openai.com/blog/dall-e/) ([paper](https://arxiv.org/abs/2102.12092)), OpenAI's Text to Image Transformer, in Pytorch.

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
        </li>
    <li>
        <span class="folder-icon">&#128193;</span>
        <span class="folder-name">Unlearning</span>
    </li>
     <li>
        <span class="folder-icon">&#128193;</span>
        <span class="folder-name">DDG Experiments</span>
    </li>
</ul>

# Results

You can Try to generate with your own fashion prompts in [Colab](https://colab.research.google.com/drive/1DzYXIfrPrri8qJmPz2WWbSLsISKf85eX)

Contact For inquiries or assistance, you can reach me at : teoaivalis@iit.demokritos.gr
