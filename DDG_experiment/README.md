# DuckDuckGo Experiments
Here is the code for the experiments with DuckDuckGo search engine.
For each of our prompts we downloaded 30 images using the API of DDG and we saved  each set of images with the relevant generated images from Midjourney Datase in folders in order to compare them and extract similarities metrics.

Our experiments can be depicted in the following figure.
![DDG Experiments](new_ddg_experiments.png)

To run the DDG experiment first you have to create the API calls and save the downladed images in a proper way so as to enable comparisons with the generated image. You have to run **create_api_calls.py**. This will create **api_calls.sh** bash script which has to be excecuded and then run. 
Data, image_list and prompts csv files contains all the information for the Midjourney dataset.

Some Examples of the DuckDuckGo experiments can be found in the following link:
[DDG_Experiments](https://drive.google.com/drive/folders/1K8A2fboCaXfwZyLH1Iu7LVgQy0hPnuzM?usp=sharing)

# Struct of the Code

<body>
    <ul>
    <li>
            <span class="file-icon">&#128196;</span>
            <span class="file-name">api_calls.sh</span>
    </li>
    <li>
            <span class="file-icon">&#128196;</span>
            <span class="file-name">create_api_calls.py</span>
   </li>
   <li>
            <span class="folder-icon">&#128193;</span>
            <span class="folder-name">data</span>
            <ul>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">data.csv</span>
                </li>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">image_list.csv</span>
                </li>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">prompts.csv</span>
                </li>
            </ul>
        </li>
    </ul>
</body>
</html>

