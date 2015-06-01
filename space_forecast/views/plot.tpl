<html>
  <head>
    <style>
    #plot td { text-align: center; }
    #plot tbody td:nth-child(5n+7) { border-left: XXX; }
    #plot td.open { background-color: green; }
    #plot td.closed { background-color: red; }
    #plot td.broken { background-color: grey; }
    </style>
  </head>
  <body>
    <table id="plot">
      <thead>
        <tr>
          <th>Date</th>
          <th colspan="72"></th>
        </tr>
      </thead>
      <tbody>
        % for week in weeks
          <tr>
            <td class="date">{{week['date']}}</td>
            % for observation in week['observations']
            <td class="{{observation['open']}}"><a href="{{observation['mirror_href']}}">(create area)</a></td>
          </tr>
      </tbody>
      <tfoot>
        <tr>
        % for hour in hours
          <td colspan="12">{{hour}}</td>
        </tr>
      </tfoot>
    </table>
  </body>
</html>
