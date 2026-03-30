def accuracy(tp, fn, fp, tn):
    return (tp + tn) / (tp + fn + fp + tn)


def true_positive_rate(tp, fn):
    return tp / (tp + fn)


def false_positive_rate(fp, tn):
    return fp / (fp + tn)


def report_group(name, tp, fn, fp, tn):
    print(name)
    print(f"  accuracy={accuracy(tp, fn, fp, tn):.3f}")
    print(f"  true_positive_rate={true_positive_rate(tp, fn):.3f}")
    print(f"  false_positive_rate={false_positive_rate(fp, tn):.3f}")
    print()


def main():
    print("Subgroup reliability metrics")
    report_group("Group A", tp=45, fn=5, fp=10, tn=40)
    report_group("Group B", tp=8, fn=12, fp=2, tn=18)


if __name__ == "__main__":
    main()
