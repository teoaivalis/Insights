# DuckDuckGo Experiments
Here is the code for the experiments with DuckDuckGo search engine.
For each of our prompts we downloaded 30 images using the API of DDG and we saved  each set of images with the relevant generated images from Midjourney Datase in folders in order to compare them and extract similarities metrics.
 
To run the DDG experiment first you have to create the API calls and save the downladed images in a proper way so as to enable comparisons with the generated image. You have to run **create_api_calls.py**. This will create **api_calls.sh** bash script which has to be excecuded and then run. 
Data, image_list and prompts csv files contains all the information for the Midjourney dataset.

# Struct of the Code



<body>
    <ul>
        <li>
            <span class="folder-icon">&#128193;</span>
            <span class="folder-name">Unlearning</span>
            <ul>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">main_experiment.py</span>
                </li>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">raw_image_similarity.py</span>
                </li>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">compare_embeddings.py</span>
                </li>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">create_ranking.py</span>
                </li>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">remove_from_dataset.py</span>
                </li>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">regenerate_images.py</span>
                </li>
                <li>
                    <span class="file-icon">&#128196;</span>
                    <span class="file-name">script1.sh</span>
                </li>
                  <li>
                    <span class="folder-icon">&#128193;</span>
                    <span class="file-name">descriptions</span>
                </li>
                <li>
                    <span class="folder-icon">&#128193;</span>
                    <span class="file-name">results</span>
                </li>
                 <li>
                    <span class="folder-icon">&#128193;</span>
                    <span class="file-name">metrics from unlearning</span>
                </li>
                 <li>
                    <span class="folder-icon">&#128193;</span>
                    <span class="file-name">Experiment 1</span>
                </li>
            </ul>
        </li>
    </ul>
</body>
</html>

