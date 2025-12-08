## Exploratory Data Analysis of Trump-related comments on Reddit
This report examines a dataset of user comments collected from Reddit. The dataset contains six months of discussions drawn from twenty different subreddits. Subreddits fall into three groups: political subreddits, Ukraine-related subreddits, and general-topic subreddits. The political subreddits include communities that support Trump, communities that oppose him, and communities that discuss political issues without a clear position.
The research focuses on how the public discusses Trump and how the tone of this discussion changes over time during the first six months of his second presidential term, depending on the events that occur around him.

Primary source: the Pushshift Reddit dataset, available on Academic Torrents: https://academictorrents.com/details/30dee5f0406da7a353aff6a8caa2d54fd01f2ca1 
Timeframe: 6 months – January 2025 to June 2025
List of subreddits: r/NeutralPolitics, r/PoliticalDebate, r/PoliticalDiscussion, r/AskReddit, r/Askpolitics, r/UkraineWarVideoReport, r/UkraineConflict, r/Conservative, r/Liberal, r/politics, r/Democrats, r/Usanews, r/ukraine, r/CringeTiktoks, r/changemyview, r/Antitrump, r/Complaints, r/Republican, r/trump, r/AskTrumpSupporters.

 see_fields.py – file for checking what parameters are available for every comment;
concat_all.py – file for merging all months to one dataset.
comments_cleanup.ipynb – some basic data checking and clean up;
eda.ipynb – final file with analysis, visualisations and conclusions;

#### These manipulations need to be performed before final EDA on the raw data downloaded from Academic Torrents: 
To decompress the received files from .zst, filter them by topic or subreddit and export them to CSV or JSON. For this task we use the scripts from https://github.com/SanGreel/PushshiftDumps. You can download the prepared dataset from https://drive.google.com/ for EDA.
