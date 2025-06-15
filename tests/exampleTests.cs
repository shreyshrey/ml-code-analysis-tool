using System.Collections.Generic;
using NUnit.Framework;
namespace Tests
{
    public class DictionaryTests
    {
        [TestCase(1)]
        public void MergeDictionariesUsingLinq()
        {
            var dict1 = new Dictionary<string, string> { { "Superman", "Flight" } };
            var dict2 = new Dictionary<string, string> { { "Batman", "Gadgets" } };

            // Using LINQ
            var merged = dict1.Concat(dict2).ToDictionary(x => x.Key, x => x.Value);

            Assert.AreEqual(3, merged.Count());
            Assert.IsTrue(merged.ContainsKey("Superman"));
            Assert.IsTrue(merged.ContainsKey("Batman"));
            Assert.AreEqual("Flight", merged["Superman"]);
            Assert.AreEqual("Gadgets", merged["Batman"]);
        }

        [TestCase(2)]
        public void MergeDictionariesUsingForeachLoop()
        {
            var dict1 = new Dictionary<string, string> { { "Superman", "Flight" } };
            var dict2 = new Dictionary<string, string> { { "Batman", "Gadgets" } };

            // Using a foreach loop
            foreach (var item in dict2)
            {
                dict1[item.Key] = item.Value;
            }

            Assert.AreEqual(2, dict1.Count());
            Assert.IsTrue(dict1.ContainsKey("Superman"));
            Assert.IsTrue(dict1.ContainsKey("Batman"));
            Assert.AreEqual("Flight", dict1["Superman"]);
            Assert.AreEqual("Gadgets", dict1["Batman"]);
        }

        [TestCase(3)]
        public void MergeDictionariesUsingUnionExtensionMethod()
        {
            var dict1 = new Dictionary<string, string> { { "Superman", "Flight" } };
            var dict2 = new Dictionary<string, string> { { "Batman", "Gadgets" } };

            // Using the Union extension method
            var merged2 = dict1.Union(dict2).ToDictionary(x => x.Key, x => x.Value);

            Assert.AreEqual(3, merged2.Count());
            Assert.IsTrue(merged2.ContainsKey("Superman"));
            Assert.IsTrue(merged2.ContainsKey("Batman"));
            Assert.AreEqual("Flight", merged2["Superman"]);
            Assert.AreEqual("Gadgets", merged2["Batman"]);
        }
    }
}