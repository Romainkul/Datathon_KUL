## **Comprehensive Project Plan: Analyzing War-Time Posters Dataset**

### **1. Data Preprocessing**

#### **1.1. Language Classification**
- **Objective:**  
  Verify and correct the language labels (Dutch, French, German) in the dataset.
- **Approach:**  
  - **Multilingual BERT or LLMs:**  
    Use a pre-trained multilingual language model (e.g., multilingual BERT) or an LLM (e.g., GPT-4) to automatically classify each OCR-extracted text.
  - **Pipeline:**  
    1. Run language detection on every text file.
    2. Compare the detected language against the folder label.
    3. Flag texts with mismatches for manual review or automated correction.
- **Example:**  
  ```python
  detected_lang, expected_code = validate_language(text, language)
  if detected_lang != expected_code:
      # Log and/or reassign the correct language label
  ```

#### **1.2. OCR Improvement with LLMs**
- **Objective:**  
  Enhance the quality of OCR outputs by correcting misrecognized characters, spacing errors, or punctuation mistakes.
- **Approach:**  
  - **LLM Post-Processing:**  
    Create a prompt that provides context about the assignment and includes the raw OCR text, then instructs the model to “clean up” the text.
  - **Prompt Example:**  
    ```
    Context: You are analyzing historical war-time posters. The following OCR output may contain errors such as misrecognized characters or misplaced punctuation. Please provide a corrected version of the text while preserving its original meaning.
    
    Text: {text}
    
    Corrected Version:
    ```
  - **Integration:**  
    Use the corrected text for all subsequent analyses.

#### **1.3. Topic, Date, and Location Extraction**
- **Objective:**  
  Extract meaningful metadata (topics, dates, locations) from the poster texts.
- **Approach:**  
  - **Rule-Based Extraction:**  
    Use regex patterns and keyword matching to extract dates (e.g., “12/05/1918”, “1 mai 1918”), locations, and the topical categories:
    - *nouvelles publiées par le Gouvernment Général allemand*
    - *avis*
    - *arreté*
    - *avertissement*
    - *explications*
  - **LLM-Assisted Extraction:**  
    Alternatively, or in parallel, craft an LLM prompt that asks for extraction of dates, locations, and topics from the provided text.
  - **NER Models:**  
    Use spaCy’s multilingual models to detect location entities (GPE, LOC, FAC) and potentially dates if formatted in text.
  
#### **1.4. Sentiment Analysis**
- **Objective:**  
  Assess the emotional tone (polarity, subjectivity) of the messages.
- **Approach:**  
  - **Multilingual Models:**  
    Use a multilingual BERT model fine-tuned for sentiment analysis or leverage LLMs to analyze sentiment.
  - **Custom Sentiment Lexicons:**  
    Consider developing or adapting sentiment lexicons specific to historical language usage.
  - **Pipeline:**  
    Process each text (or aggregated texts per topic/language) to generate sentiment scores that can be tracked over time.

---

### **2. Data Exploration**

#### **2.1. Wordcloud Generation**
- **Objective:**  
  Visualize the most frequent words in each language or topic.
- **Approach:**  
  - Create wordclouds for each language’s aggregated texts.
  - Optionally generate topic-specific wordclouds (e.g., for “avis” or “arreté”) to see distinct vocabularies.

#### **2.2. Multi-Modal Visualization with CLIP**
- **Objective:**  
  Visualize poster images in a reduced feature space to identify clusters based on visual style or propaganda techniques.
- **Approach:**  
  - **CLIP Encoding:**  
    Use CLIP to extract visual features from the raw images.
  - **Dimensionality Reduction:**  
    Apply techniques like PCA, t-SNE, or UMAP to reduce the feature dimensions.
    - *Note:* You mentioned “the other one forgot name” — UMAP is a great candidate.
  - **Clustering:**  
    Use K-Means or DBSCAN to cluster images.
  - **Visualization:**  
    Create scatter plots of the reduced-dimension features, color-coded by cluster.
  - **Integration:**  
    Compare these clusters with the topic and sentiment clusters from text analysis.

---

### **3. Data Analysis**

#### **3.1. Time Series Analysis of Polarity of Messages**
- **Objective:**  
  Track how sentiment (polarity) evolves over time as the war progresses.
- **Approach:**  
  - **Extract Time Information:**  
    Use the dates extracted from the texts to build a timeline.
  - **Aggregate Sentiment Data:**  
    Calculate average polarity scores for each time interval (e.g., monthly or yearly).
  - **Visualization:**  
    Plot a time series graph of sentiment polarity.
  - **Correlation:**  
    Explore correlations between sentiment changes and key historical events.

#### **3.2. Comparative Analysis Across Topics and Languages**
- **Objective:**  
  Understand differences in messaging and tone across the topical categories and languages.
- **Approach:**  
  - Compare word usage, sentiment, and visual styles among different topics.
  - Analyze whether messages from “nouvelles publiées par le Gouvernment Général allemand” have different sentiment trajectories compared to “avertissement” or “avis.”
  - Consider cross-language comparisons to see if, for instance, French posters have different emotional tones or visual strategies compared to German or Dutch posters.

#### **3.3. Propaganda Technique Classification and Narrative Generation**
- **Objective:**  
  Identify propaganda techniques and generate narrative summaries.
- **Approach:**  
  - **Unsupervised Clustering:**  
    Use sentence embeddings (e.g., with SentenceTransformer) and clustering (K-Means, DBSCAN) to group texts into propaganda technique clusters.
  - **LLM Narrative Generation:**  
    Use an LLM to generate historical narratives from clusters of texts, providing context and summarizing key themes.
  - **Scenario Simulation:**  
    Optionally, generate “what-if” scenarios to explore how messaging might have differed under alternate conditions.

---

### **4. Additional Creative Extensions**

#### **4.1. Interactive Dashboard**
- **Objective:**  
  Create an interactive tool for stakeholders (e.g., historians, researchers) to explore the dataset.
- **Approach:**  
  - Build a dashboard using Streamlit, Dash, or Panel.
  - Allow users to filter data by language, topic, date, sentiment, or visual cluster.
  - Enable drill-down into individual posters, showing both the original image and the corrected OCR text, along with extracted metadata.
  - Integrate interactive time series and geographical maps.

#### **4.2. External Data Integration**
- **Objective:**  
  Enhance analysis by linking the dataset with external historical data.
- **Approach:**  
  - Merge the dataset with external archives (e.g., news articles, battle records, government announcements).
  - Analyze how poster messages correlate with contemporaneous events.
  - Create visual overlays (e.g., on maps or timelines) showing external events alongside changes in sentiment or topic distributions.

---

### **5. Reporting and Documentation**

- **Documentation:**  
  Document each step of the pipeline—from data preprocessing to analysis—and include the rationale for model and method choices.
- **Visual Reporting:**  
  Create a comprehensive report with:
  - Wordclouds and visualizations of image clusters.
  - Time series graphs of sentiment polarity.
  - Comparative analyses across topics and languages.
  - Narratives generated by LLMs, with contextual historical analysis.
- **Final Presentation:**  
  Prepare a report
