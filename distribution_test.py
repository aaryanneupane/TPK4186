from module.Edge import Edge
from module.Distribution import Distribution

# test_edge = Edge("test", length=30)
# test_edge.distribution["Monday"].addPoint((17, 34))
# test_edge.distribution["Monday"].addPoint((124, 30))
# test_edge.distribution["Monday"].addPoint((600, 31))
# test_edge.distribution["Monday"].addPoint((900, 33))

# print(test_edge.distribution["Monday"].closest_time(200))
# print(test_edge.distribution["Monday"].interpolate(1000))

test_dist = EmpiricalDistribution()
test_dist.generate_distribution_constant()
print(test_dist.points)


