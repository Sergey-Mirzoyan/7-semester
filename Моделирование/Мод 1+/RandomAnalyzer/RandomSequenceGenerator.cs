using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace RandomAnalyzer
{
    public class RandomSequenceGenerator
    {
        private readonly Random random = new Random();

        public IList<int> GetSequence(int min, int max, int count)
        {
            if (count < 0)
                throw new ArgumentOutOfRangeException("count");
            if (min >= max)
                throw new ArgumentException("min, max");

            int realMax = max + 1;
            var res = new int[count];
            for (int i = 0; i < count; ++i)
                res[i] = random.Next(min, realMax);
            return res;
        }
    }
}
