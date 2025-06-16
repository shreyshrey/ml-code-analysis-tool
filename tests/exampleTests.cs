csharp
using NUnit.Framework;

[TestFixture]
public class DictionaryMergeTests
{
    [Test]
    public void Test_MergingDictionaries_UsingConcat()
    {
        // Arrange
        var dict1 = new Dictionary<string, string> { { "Superman", "Flight" } };
        var dict2 = new Dictionary<string, string> { { "Batman", "Gadgets" } };

        // Act
        var merged = dict1.Concat(dict2).ToDictionary(x => x.Key, x => x.Value);

        // Assert
        #Test case 1:
        Assert.AreEqual("Flight", merged["Superman"]);
        #Test case 2:
        Assert.AreEqual("Gadgets", merged["Batman"]);
    }

    [Test]
    public void Test_MergingDictionaries_UsingForeach()
    {
        // Arrange
        var dict1 = new Dictionary<string, string> { { "Superman", "Flight" } };
        var dict2 = new Dictionary<string, string> { { "Batman", "Gadgets" } };

        // Act
        foreach (var item in dict2)
        {
            dict1[item.Key] = item.Value;
        }

        // Assert
        #Test case 3:
        Assert.AreEqual("Flight", dict1["Superman"]);
        #Test case 4:
        Assert.AreEqual("Gadgets", dict1["Batman"]);
    }

    [Test]
    public void Test_MergingDictionaries_UsingUnion()
    {
        // Arrange
        var dict1 = new Dictionary<string, string> { { "Superman", "Flight" } };
        var dict2 = new Dictionary<string, string> { { "Batman", "Gadgets" } };

        // Act
        var merged = dict1.Union(dict2).ToDictionary(x => x.Key, x => x.Value);

        // Assert
        #Test case 5:
        Assert.AreEqual("Flight", merged["Superman"]);
        #Test case 6:
        Assert.AreEqual("Gadgets", merged["Batman"]);
    }
}