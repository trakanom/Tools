using System;

namespace FizzBuzz
{
    class Program
    {
        public static void Main(string[] args)
        {
            Program x = new Program();
            // Console.WriteLine("Hello World!");
            string[] solution = x.FizzBuzz(15);
            foreach (string thing in solution)
            {
                Console.WriteLine(thing);
            }
        }
        public string[] FizzBuzz(int n)
        {
            string[] answers = { "hi", "bye" };
            // int stringSize = n;
            answers = new string[n];
            for (int i = 1; i <= n; i++)
            {
                answers[(i - 1)] = "";
                if (i % 3 == 0)
                {
                    // thisanswer = "Fizz";
                    answers[(i - 1)] = "Fizz";
                }
                if (i % 5 == 0)
                {
                    // thisanswer += "Buzz";
                    answers[(i - 1)] += "Buzz";
                }
                if (i % 3 != 0 && i % 5 != 0)
                {
                    // thisanswer += i;
                    answers[(i - 1)] += i;
                }
                // Console.WriteLine(thisanswer);
            }

            return answers;
        }
    }
}
