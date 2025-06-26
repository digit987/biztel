from collections import Counter

class ChatAnalyzer:
    def __init__(self, chat_data):
        self.chat_data = chat_data

    def summarize(self):
        agent1_msgs = [x for x in self.chat_data if x['agent'] == 'agent_1']
        agent2_msgs = [x for x in self.chat_data if x['agent'] == 'agent_2']

        return {
            "article_url": self.chat_data[0].get("article_url", "Unknown"),
            "agent_1_messages": len(agent1_msgs),
            "agent_2_messages": len(agent2_msgs),
            "agent_1_sentiments": dict(Counter([x['sentiment'] for x in agent1_msgs])),
            "agent_2_sentiments": dict(Counter([x['sentiment'] for x in agent2_msgs]))
        }