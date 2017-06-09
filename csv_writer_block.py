from nio.block.base import Block
from nio.properties import Property, FileProperty, VersionProperty, BoolProperty
import csv


class CSVWriter(Block):

    file = FileProperty(title='File', default='output.csv')
    row = Property(title='Row', default='')
    overwrite = BoolProperty(title='Overwrite File?', default=False)
    version = VersionProperty('0.1.0')

    def process_signals(self, signals):
        for signal in signals:
            file_name = self.file(signal).value
            data = self.row(signal)
            if not isinstance(data, list):
                self.logger.error('row must evaluate to a list')
                continue
            # csv module requires file objects be opened with newline=''
            if self.overwrite():
                with open(file_name, 'w', newline='') as csvfile:
                    self.logger.debug('{} opened'.format(file_name))
                    csv.writer(csvfile).writerow(data)
                    self.logger.debug('{} appended to end of file'.format(data))
            else:
                with open(file_name, 'a', newline='') as csvfile:
                    self.logger.debug('{} opened'.format(file_name))
                    csv.writer(csvfile).writerow(data)
                    self.logger.debug('{} appended to end of file'.format(data))
