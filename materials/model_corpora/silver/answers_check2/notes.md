# Silver check2 independent-label notes

Labels were assigned from `LABEL_GUIDE.md` v2.1, without consulting the silver mapping, training labels, previous answers, or model predictions.

- k0006 / k0056 / k0120 / k0174 / k0429: `other` — treated Gini coefficient as a statistical metric, not a rate or percentage.
- k0051: `unknown` — the header is absent and the lone value “Credit Cards Accepted” does not identify the column type.
- k0073: `text` — the values are generic name-search phrases, not identifiable organization names or a fixed controlled category.
- k0119 / k0143 / k0323 / k0436: `unknown` — bare numbers without a header, unit, or table context do not distinguish a count, amount, or measurement.
- k0183: `amount` — the values are salary-like numbers and one sample explicitly says “Starting salary”.
- k0233: `other` — the values are named wars, battles, and historical events; they do not express a listed type or free-form description.
- k0269: `id` — ISO 3166-2 values identify administrative subdivisions; treated as identifiers rather than country names/codes.
- k0299: `org` — the named transport network is treated as a transit service entity.
- k0312: `org` — the named open-data portals are treated as portal/service entities.
- k0356: `id` — ABC News topic values are source topic slugs in an explicit ID field, even though the slugs are readable words.
- k0363: `quantity` — “orbits completed” is a count; the value 2020 is interpreted as a count, not a year.
- k0370: `other` — the values are Unicode flag glyphs, not country names or country-code strings.
- k0377: `text` — the values are named response/event descriptions rather than a small fixed set of status categories.
- k0401: `text` — the values are route-diagram template names, treated as resource titles.
- k0412: `category` — “EventScheduled” is a fixed event-status value.
- k0417: `unknown` — the lone value “Athletic” without a header or table context is ambiguous.
- k0463: `category` — the values combine occupational classification codes and class descriptions.
- k0473: `address` — the taxon-range examples are named geographic places.
