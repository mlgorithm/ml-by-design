import numpy as np


def convolve2d(image, kernel):
    height, width = image.shape
    kernel_height, kernel_width = kernel.shape
    output = np.zeros((height - kernel_height + 1, width - kernel_width + 1))
    for row in range(output.shape[0]):
        for col in range(output.shape[1]):
            patch = image[row : row + kernel_height, col : col + kernel_width]
            output[row, col] = np.sum(patch * kernel)
    return output


def max_pool2d(feature_map, pool_size=2):
    pooled_height = feature_map.shape[0] // pool_size
    pooled_width = feature_map.shape[1] // pool_size
    pooled = np.zeros((pooled_height, pooled_width))
    for row in range(pooled_height):
        for col in range(pooled_width):
            patch = feature_map[
                row * pool_size : (row + 1) * pool_size,
                col * pool_size : (col + 1) * pool_size,
            ]
            pooled[row, col] = np.max(patch)
    return pooled


def main():
    original_image = np.array(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
        dtype=float,
    )
    shifted_image = np.array(
        [
            [0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ],
        dtype=float,
    )
    vertical_edge_filter = np.array(
        [
            [-1, 0, 1],
            [-1, 0, 1],
            [-1, 0, 1],
        ],
        dtype=float,
    )

    for name, image in [("original", original_image), ("shifted", shifted_image)]:
        feature_map = convolve2d(image, vertical_edge_filter)
        pooled = max_pool2d(feature_map, pool_size=2)
        print(name)
        print("image:")
        print(image)
        print("feature_map:")
        print(feature_map)
        print("pooled:")
        print(pooled)
        print(f"global_max_response={feature_map.max():.1f}")
        print()


if __name__ == "__main__":
    main()
