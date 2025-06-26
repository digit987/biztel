import pandas as pd

class DataTransformer:
    def flatten_conversations(self, data):
        records = []
        for conv_id, conv_data in data.items():
            for turn in conv_data['content']:
                records.append({
                    'conversation_id': conv_id,
                    'agent': turn['agent'],
                    'message': turn['message'],
                    'sentiment': turn['sentiment'],
                    'knowledge_source': turn['knowledge_source'],
                    'turn_rating': turn['turn_rating'],
                    'article_url': conv_data['article_url'],
                })
        return pd.DataFrame(records)