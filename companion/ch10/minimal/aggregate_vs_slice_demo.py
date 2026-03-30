def accuracy(correct, total):
    return correct / total


def main():
    slice_a_correct = 95
    slice_a_total = 100
    slice_b_correct = 15
    slice_b_total = 30

    overall_correct = slice_a_correct + slice_b_correct
    overall_total = slice_a_total + slice_b_total

    print("Aggregate versus slice evaluation")
    print(f"  overall_accuracy={accuracy(overall_correct, overall_total):.3f}")
    print(f"  slice_a_accuracy={accuracy(slice_a_correct, slice_a_total):.3f}")
    print(f"  slice_b_accuracy={accuracy(slice_b_correct, slice_b_total):.3f}")


if __name__ == "__main__":
    main()
