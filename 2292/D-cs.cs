using System.ComponentModel.DataAnnotations;
using System.Linq;

namespace DefaultNamespace;

public class Program
{
    static void Main()
    {
        var t = int.Parse(Console.ReadLine());
        
        for (int _ = 0; _ < t; _++)
        {
            var n = int.Parse(Console.ReadLine());
            var left = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);
            var right = Array.ConvertAll(Console.ReadLine().Split(), int.Parse);

            var dp = new long[n + 1, 2];

            for (int i = n - 1; i > -1; i--)
            {
                var diff = left[i] - right[i];

                dp[i, 0] = Math.Max(dp[i + 1, 1], dp[i + 1, 0] + diff);
                dp[i, 1] = Math.Min(dp[i + 1, 0], dp[i + 1, 1] - diff);
            }

            if (dp[0, 0] < 0) Console.WriteLine("Aubrey");
            else if (dp[0, 0] > 0) Console.WriteLine("Sunny");
            else Console.WriteLine("Draw");
        }
    }
}