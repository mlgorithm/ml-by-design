import math


def dcg(relevances):
    return sum(rel / math.log2(rank + 2) for rank, rel in enumerate(relevances))


def ndcg(relevances):
    ideal = sorted(relevances, reverse=True)
    ideal_dcg = dcg(ideal)
    if ideal_dcg == 0.0:
        return 0.0
    return dcg(relevances) / ideal_dcg


def exposure_weight(rank):
    return 1.0 / math.log2(rank + 2)


def main():
    relevance_by_item = {
        "worked-example": 3,
        "short-video": 2,
        "practice-quiz": 3,
        "forum-thread": 1,
        "syllabus-page": 0,
    }
    ranker_a = ["worked-example", "practice-quiz", "short-video", "forum-thread", "syllabus-page"]
    ranker_b = ["syllabus-page", "forum-thread", "short-video", "practice-quiz", "worked-example"]

    for name, ranking in [("A", ranker_a), ("B", ranker_b)]:
        relevances = [relevance_by_item[item] for item in ranking]
        print(f"ranker {name}")
        print(f"  ranking={ranking}")
        print(f"  relevances={relevances}")
        print(f"  dcg={dcg(relevances):.3f} ndcg={ndcg(relevances):.3f}")
        print("  exposure weights")
        for rank, item in enumerate(ranking, start=1):
            print(
                f"    rank={rank} item={item:15s} "
                f"relevance={relevance_by_item[item]} "
                f"exposure={exposure_weight(rank - 1):.3f}"
            )
        print()

    print("audit note")
    print(
        "A click log observes feedback only for items the system exposed. "
        "A non-click on an unshown item is missing data, not evidence of dislike."
    )


if __name__ == "__main__":
    main()
