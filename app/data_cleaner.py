class DataCleaner:
    def clean(self, data_dict):
        cleaned = {}
        for k, v in data_dict.items():
            if 'content' in v and isinstance(v['content'], list):
                cleaned[k] = v
        return cleaned