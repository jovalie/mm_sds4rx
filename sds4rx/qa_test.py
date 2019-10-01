from mindmeld.components import QuestionAnswerer
qa = QuestionAnswerer('.')
qa.load_kb('sds4rx', '50_common_rx', './data/50_common_rx.json')