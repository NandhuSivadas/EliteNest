import io
import base64
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from textblob import TextBlob
from django.shortcuts import render
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from User.models import * 

def analyze_sentiment(review):
    analysis = TextBlob(review)
    if analysis.sentiment.polarity > 0:
        return 'Positive'
    elif analysis.sentiment.polarity < 0:
        return 'Negative'
    else:
        return 'Neutral'

@csrf_exempt
def homepage(request):
    if request.method == 'POST':
      
        reviews = tbl_review.objects.all().values('review')
        df = pd.DataFrame(list(reviews))

       
        df['sentiment'] = df['review'].apply(analyze_sentiment)
        sentiment_counts = df['sentiment'].value_counts()

      
        fig, axes = plt.subplots(2, 2, figsize=(12, 8))

       
        sns.barplot(x=sentiment_counts.index, y=sentiment_counts.values, palette='viridis', ax=axes[0, 0], hue=None, legend=False)
        axes[0, 0].set_title('Sentiment Distribution')
        axes[0, 0].set_xlabel('Sentiment')
        axes[0, 0].set_ylabel('Count')

       
        axes[0, 1].pie(sentiment_counts, labels=sentiment_counts.index, autopct='%1.1f%%', colors=sns.color_palette('viridis', n_colors=len(sentiment_counts)))
        axes[0, 1].set_title('Sentiment Proportion')

      
        sentiment_data = pd.DataFrame({'Sentiment': sentiment_counts.index, 'Count': sentiment_counts.values})
        sentiment_data['Percentage'] = (sentiment_data['Count'] / sentiment_data['Count'].sum()) * 100

        sentiment_data.plot(kind='bar', x='Sentiment', y=['Count'], stacked=True, color=sns.color_palette('viridis', n_colors=len(sentiment_counts)), ax=axes[1, 0])
        axes[1, 0].set_title('Sentiment Stacked Bar Chart')
        axes[1, 0].set_xlabel('Sentiment')
        axes[1, 0].set_ylabel('Count')

      
        fig.delaxes(axes[1, 1])

        
        plt.tight_layout()

        
        buffer = io.BytesIO()
        canvas = FigureCanvas(fig)
        canvas.print_png(buffer)
        plt.close(fig)

        
        plot_data = base64.b64encode(buffer.getvalue()).decode('utf-8')
        return JsonResponse({'plot_data': plot_data})

    return render(request, 'ML/HomePageReview.html')
