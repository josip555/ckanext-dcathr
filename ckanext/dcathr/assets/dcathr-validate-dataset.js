"use strict";

this.ckan.module("dcathr-validate-dataset", function ($) {
  return {
    options: {
      content: '',
    },

    initialize: function () {
      jQuery.proxyAll(this, /_on/);
        this.el.on('click', this._onClick);
    },

    validateDataset: function () {
      var queryParameters = "?shapeModel=dcatap211";
      var apiUrl = "https://data.europa.eu/api/mqa/shacl/validation/report" + queryParameters;
      var reportEl = document.getElementById("validation-report");
      reportEl.textContent = "Validating...";

      var request = $.ajax({
        url: apiUrl,
        method: "POST",
        data: this.options.content,
        dataType: "text",
        contentType: "text/xml",
      });
      request.done(function( data ) {
        var report = JSON.parse(data);
        var reportGraph = report['@graph'];

        if (report['shacl:conforms'] && report['shacl:conforms']['@value'] === "true") reportEl.textContent = "Dataset is DCAT-AP-compliant.";
        else {
          var numResults = reportGraph.length - 1;
          var conforms = "false";

          reportEl.textContent = "Invalid dataset schema (" + numResults + " messages):";
          reportEl.appendChild(document.createElement("br"));
          reportEl.appendChild(document.createElement("br"));
          var reportElList = reportEl.appendChild(document.createElement("ul"));

          for(let i = 0; i < reportGraph.length; i++) {
            if(!reportGraph[i]['shacl:resultPath']) continue;
            let resPathSplit = reportGraph[i]['shacl:resultPath']['@id'].split("/");
            let reportElItem = reportElList.appendChild(document.createElement("li"));
            
            reportElItem.innerHTML = "Issue in property " + resPathSplit[resPathSplit.length - 1].bold()
              + " of node " + reportGraph[i]['shacl:focusNode']['@id'].bold() + "<br />" + reportGraph[i]['shacl:resultMessage'];
          };
        }
      });
      request.fail(function( jqXHR, textStatus ) {
        reportEl.textContent = "Request failed: " + textStatus;
      });
    },

    _onClick: function (event) {
      event.preventDefault();
      this.validateDataset();
    },
  };
});
