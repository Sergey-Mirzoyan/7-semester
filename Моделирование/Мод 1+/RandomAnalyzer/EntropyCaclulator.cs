using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RandomAnalyzer
{
    public static class EntropyCaclulator
    {
        public static double CalculateEntropy(IEnumerable<int> sequence)
        {
            var data = sequence.GroupBy(x => x)
                .Select(x => x.Count());
            double sum = data.Sum();
            double logBase = Math.Max(2, data.Count());
            return data.Select(x => x / sum)
                .Sum(x => -x * Math.Log(x, logBase));
        }

        public static double CaclulateDifferenceEntropy(IEnumerable<int> sequence)
        {
            return CalculateEntropy
                (
                    sequence.Zip(sequence.Skip(1), (first, second) => second - first)
                );
        }
    }
}
