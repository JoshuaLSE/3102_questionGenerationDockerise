from pipelines import pipeline

if __name__ == '__main__':
    # nlp = pipeline("question-generation")
    nlp = pipeline("e2e-qg")  # Use this pipeline instead
    text = "All that is gold does not glitter,Not all those who wander are lost,The old that is strong does not " \
           "wither,Deep roots are not reached by the frost. From the ashes a fire shall be woken, A light from the " \
           "shadows shall spring; Renewed shall be blade that was broken, The crownless again shall be king. "
    print(nlp(text))
