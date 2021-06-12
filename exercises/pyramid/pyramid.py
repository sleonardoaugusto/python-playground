def build_pyramid(height, pyramid=None):
    if not pyramid:
        pyramid = []

    if len(pyramid) == height:
        return '\n'.join(pyramid)
    else:
        pyramid.append('0' * (len(pyramid) + 1))
        return build_pyramid(height, pyramid)
