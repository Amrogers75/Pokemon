"use strict"

var SCRAPE_URL = "http://www.pokemon.com/us/pokemon-tcg/pokemon-cards/";

var scraper = require('pokemon-tcg-scraper')
var request = require('request-promise');
var cheerio = require('cheerio');
var Promise = require('bluebird');
var co = Promise.coroutine;
var trim = require('trim');
var Url = require('url');
var qs = require('querystring');
var capitalize = require('capitalize');
var _ = require('lodash');
./
function makeUrl(url, query) {
    return url + "?" + qs.stringify(query);
}

function cardIdFromUrl(url){
   return url.match(new RegExp("/(\\w+/\\w+)/$"))[1];
}

function scrapeAll(query, scrapeDetails) {

    return co(function *() {
        //By default, scrape the card details
        scrapeDetails = scrapeDetails === undefined ? true : scrapeDetails;

        //Load the HTML page
        process.stdout.write("Scraping initial page...");
        var scrapeURL = makeUrl(SCRAPE_URL, query);
        var search = yield scrapeSearchPage(scrapeURL);
        process.stdout.write("Done!\n");

        //Recurring variables
        var cards = search.cards;
        var i;

        //Scrape all of the pages sequentially;
        process.stdout.write('Scraping card URLs...\n');
        for (i = 2; i <= search.numPages; i++) {
            process.stdout.write('   Scraping page ' + i + '...');
            var scrapeURL = makeUrl(Url.resolve(SCRAPE_URL, i.toString()), query);
            var results = yield scrapeSearchPage(scrapeURL);
            cards = cards.concat(results.cards);
            process.stdout.write('Done!\n');
        }

        //Scrape all of the cards sequentially if requested
        if (scrapeDetails) {
            process.stdout.write('Scraping card details...\n');
            for (i = 0; i < cards.length; i++) {
                var card = cards[i];
                process.stdout.write('   Scraping card ' + card.url);
                _.assign(card, yield scrapeCard(card));
                process.stdout.write('Done!\n')
            }
        }

        return cards;
    })();
}

module.exports = {
    scrapeAll: scrapeAll,
    scrapeCard: scrapeCard,
    scrapeSearchPage: scrapeSearchPage
};