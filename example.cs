Dictionary<string, string> dict1 = new Dictionary<string, string> { { "Superman", "Flight" } };
Dictionary<string, string> dict2 = new Dictionary<string, string> { { "Batman", "Gadgets" } };

// Using LINQ
var merged = dict1.Concat(dict2).ToDictionary(x => x.Key, x => x.Value);

// Using a foreach loop
foreach (var item in dict2)
{
    dict1[item.Key] = item.Value;
}

// Using the Union extension method
var merged2 = dict1.Union(dict2).ToDictionary(x => x.Key, x => x.Value);