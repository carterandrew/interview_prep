import unittest

def acmTeam(topic):
    topic_count = {}
    max_topics = 0
    for i in range(len(topic) - 1):
        for j in range(i+1, len(topic)):
            t1 = topic[i]
            t2 = topic[j]
            combined = bin(int(t1, 2) | int(t2, 2)).count("1")
            if combined not in topic_count:
                topic_count[combined] = 0
            topic_count[combined] += 1
            if combined > max_topics:
                max_topics = combined
    return [max_topics, topic_count[max_topics]]


class testAcmTeam(unittest.TestCase):

    def testSameTopics(self):
        people = ['100', '100']
        self.assertEqual(acmTeam(people), [1, 1])

    def testFiveTopics(self):
        people = ['10101', '11100', '11010', '00101']
        self.assertEqual(acmTeam(people), [5, 2])


if __name__ == '__main__':
    unittest.main()
